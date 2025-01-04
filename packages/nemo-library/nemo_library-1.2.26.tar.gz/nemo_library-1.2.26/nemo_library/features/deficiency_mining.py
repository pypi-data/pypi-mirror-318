import logging
import os
import pandas as pd
from nemo_library.features.config import Config
from nemo_library.features.focus import _get_attribute_tree
from nemo_library.features.projects import (
    createOrUpdateReport,
    createOrUpdateRule,
    getImportedColumns,
)
from nemo_library.utils.utils import get_internal_name


def createOrUpdateRulesByConfigFile(
    config: Config,
    filename: str,
) -> None:

    # read file
    configdf = _import_xlsx_file(filename)

    logging.info(
        f"file '{filename}' sucessfully imported. {len(configdf)} records found"
    )

    # outer loop: projects
    projects = configdf["NEMO_PROJECT_NAME"].unique().tolist()
    for project_name in projects:
        _process_project(
            config=config,
            configdf=configdf,
            project_name=project_name,
        )

def _process_project(
    config: Config,
    configdf: pd.DataFrame,
    project_name: str,
) -> str:

    logging.info(f"working on project '{project_name}'")

    # next level: same restrictions
    restrictions = (
        configdf[configdf["NEMO_PROJECT_NAME"] == project_name][
            "NEMO_DEFICIENCY_RESTRICTIONS"
        ]
        .unique()
        .tolist()
    )
    for restriction in restrictions:
        _process_restriction(
            config=config,
            configdf=configdf,
            project_name=project_name,
            restriction=restriction,
        )


def _process_restriction(
    config: Config,
    configdf: pd.DataFrame,
    project_name: str,
    restriction: str,
) -> None:
    logging.info(f"working on project '{project_name}', restriction '{restriction}'")

    filtereddf = configdf[
        (configdf["NEMO_PROJECT_NAME"] == project_name)
        & (configdf["NEMO_DEFICIENCY_RESTRICTIONS"] == restriction)
    ]

    # read values from df and check whether the values are unique
    restriction_description = _validate_restriction(
        filtereddf, project_name, "NEMO_DEFICIENCY_RESTRICTIONS_DESCRIPTION"
    )[0]
    restriction_excpetion = _validate_restriction(
        filtereddf, project_name, "NEMO_DEFICIENCY_EXCEPTIONS"
    )[0]
    report_field_groups = _validate_restriction(
        filtereddf, project_name, "NEMO_DEFICIENCY_REPORT_FIELD_GROUPS"
    )
    report_field_list = _validate_restriction(
        filtereddf, project_name, "NEMO_DEFICIENCY_REPORT_FIELD_LIST"
    )
    report_field_except_list = _validate_restriction(
        filtereddf, project_name, "NEMO_DEFICIENCY_REPORT_EXCEPT_LIST"
    )
    
    # resolve field groups into field list
    report_field_list = (
        _resolve_field_groups(
            config=config, project_name=project_name, field_groups=report_field_groups
        )
        if report_field_groups
        else [] + report_field_list if report_field_list else []
    )

    # eliminate douplicates and remove except fields
    report_field_list = list(set(report_field_list) - set(report_field_except_list if report_field_except_list else []))

    # fields found?
    if not report_field_list:
        raise ValueError("Field list is empty!")

    # validate fields given
    internal_names_NEMO = getImportedColumns(config=config, projectname=project_name)[
        "internalName"
    ].to_list()
    fields_not_existing = set(report_field_list) - set(internal_names_NEMO)
    if fields_not_existing:
        raise ValueError(
            f"One or many fields not found in project: {fields_not_existing}"
        )

    global_frags_check = []
    global_frags_msg = []

    # process fields now
    field_list = filtereddf["NEMO_INTERNAL_NAME"].unique().tolist()
    for field in field_list:
        fieldsdf = filtereddf[filtereddf["NEMO_INTERNAL_NAME"] == field]
        (fieldfrags_check, field_frags_msg) = _process_field(
            config=config,
            project_name=project_name,
            restriction=restriction,
            restriction_description=restriction_description,
            restriction_excpetion=restriction_excpetion,
            field=field,
            report_field_list=report_field_list,
            fieldsdf=fieldsdf,
        )
        global_frags_check.append(fieldfrags_check)
        global_frags_msg.append(field_frags_msg)


def _process_field(
    config: Config,
    project_name: str,
    restriction: str,
    restriction_description: str,
    restriction_excpetion: str,
    field: str,
    report_field_list: list[str],
    fieldsdf: pd.DataFrame,
) -> (list[str], list[str]):
    logging.info(
        f"working on project '{project_name}', restriction '{restriction}', field '{field}'"
    )
    field_frags_check = []
    field_frags_msg = []
    for idx, row in fieldsdf.iterrows():
        field_frags_check.append(f"({row["NEMO_DEFICIENCY_RULE_DEFINITION"]})")
        field_frags_msg.append(
            f"WHEN ({row["NEMO_DEFICIENCY_RULE_DEFINITION"]}) THEN '{row['NEMO_INTERNAL_NAME']} {row['NEMO_DEFICIENCY_RULE_NAME']}'"
        )

    select = f"""SELECT 
\tCASE WHEN
\t\t{"\n\t\t  OR ".join(field_frags_check)} THEN 'check' ELSE 'ok'
\tEND AS STATUS
\t, CASE {"\n\t\t".join(field_frags_msg)} END AS DEFICIENCY_MESSAGE
\t, {"\n\t, ".join([field] + [fieldr for fieldr in report_field_list if fieldr != field ])}
FROM
    $schema.$table
WHERE
    ({restriction})
AND ({restriction_excpetion})
"""

    # create the report
    report_display_name = f"(DEFICIENCIES) {restriction_description} {field}"
    report_internal_name = get_internal_name(report_display_name)

    createOrUpdateReport(
        config=config,
        projectname=project_name,
        displayName=report_display_name,
        internalName=report_internal_name,
        querySyntax=select,
        description=f"Deficiency Mining Report for restriction {restriction_description} column '{field}' in project '{project_name}'",
    )

    createOrUpdateRule(
        config=config,
        projectname=project_name,
        displayName=f"{restriction_description} {field}",
        ruleSourceInternalName=report_internal_name,
        ruleGroup=restriction_description,
        description=f"Deficiency Mining Report for restriction {restriction_description} column '{field}' in project '{project_name}'",
    )
    return field_frags_check, field_frags_msg


def _resolve_field_groups(
    config: Config, project_name: str, field_groups: list[str]
) -> list[str]:
    df = _get_attribute_tree(config=config, projectname=project_name)
    group_internal_names = df["groupInternalName"].unique().tolist()
    groups_not_existing = set(field_groups) - set(group_internal_names)
    if groups_not_existing:
        raise ValueError(
            f"One or many field groups not found in project: {groups_not_existing}"
        )

    filtereddf = df[df["groupInternalName"].isin(field_groups)]
    internalColumnName = filtereddf["internalColumnName"].to_list()
    return internalColumnName


def _validate_restriction(
    filtereddf: pd.DataFrame,
    project_name: str,
    field_name: str,
) -> list[str]:
    field_value = filtereddf[field_name].unique().tolist()
    if len(field_value) != 1:
        raise ValueError(
            f"project: {project_name}, restriction: {filtereddf['NEMO_DEFICIENCY_RESTRICTIONS'].iloc[0][0]}: {field_name} is not unique.\nValues provided: {field_value}\nPlease ensure that all records with same project name and same restriction have all the same value in this field"
        )
    return str(field_value[0]).split(",") if not pd.isnull(field_value[0]) else None


def _import_xlsx_file(
    filename: str,
) -> pd.DataFrame:

    # validate file
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)

    # import file
    df = pd.read_excel(filename)

    # check columns
    expected_columns = [
        "NEMO_RULE_ID",
        "NEMO_PROJECT_NAME",
        "NEMO_DEFICIENCY_RESTRICTIONS",
        "NEMO_DEFICIENCY_RESTRICTIONS_DESCRIPTION",
        "NEMO_DEFICIENCY_REPORT_FIELD_GROUPS",
        "NEMO_DEFICIENCY_REPORT_FIELD_LIST",
        "NEMO_DEFICIENCY_REPORT_EXCEPT_LIST",
        "NEMO_INTERNAL_NAME",
        "NEMO_DEFICIENCY_RULE_DEFINITION",
        "NEMO_DEFICIENCY_RULE_NAME",
        "NEMO_DEFICIENCY_CATEGORY",
        "NEMO_DEFICIENCY_RULE_DESCRIPTION",
        "NEMO_DEFICIENCY_EXCEPTIONS",
    ]

    actual_columns = df.columns.to_list()

    missing_columns = set(expected_columns) - set(actual_columns)
    extra_columns = set(actual_columns) - set(expected_columns)

    if missing_columns or extra_columns:
        print(df.columns.to_list())
        raise ValueError(
            f"Headers do not match!\n"
            f"Missing columns: {', '.join(missing_columns) if missing_columns else 'None'}\n"
            f"Extra columns: {', '.join(extra_columns) if extra_columns else 'None'}"
        )

    return df
