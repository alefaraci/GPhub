# FILES GENERATOR

import subprocess
import packages.List as pk


def get_Language(packages, framework) -> str:
    Language = ""
    if len(packages[framework]["Language"]) == 1:
        Language += f"""$("#{framework}Language").load("/languages/{packages[framework]["Language"][0]}.html");"""
    else:
        for i, _ in enumerate(packages[framework]["Language"]):
            if i == 0:
                Language += f"""$("#{framework}Language{i+1}").load("/languages/{packages[framework]["Language"][i]}.html");\n"""
            else:
                Language += f"""\t\t$("#{framework}Language{i+1}").load("/languages/{packages[framework]["Language"][i]}.html");\n"""
    return Language


def get_License(packages, framework) -> str:
    License = ""
    if len(packages[framework]["License"]["type"]) == 1:
        License += f"""$("#{framework}License").load("/licenses/{packages[framework]["License"]["type"][0]}.html" , function () {{
            $("#{framework}License a").attr("href", "{packages[framework]['License']['URL'][0]}");
        }})"""
    else:
        for i, _ in enumerate(packages[framework]["License"]["type"]):
            if i == 0:
                License += f"""$("#{framework}License{i+1}").load("/licenses/{packages[framework]["License"]["type"][i]}.html" , function () {{
                    $("#{framework}License{i+1} a").attr("href", "{packages[framework]['License']['URL'][i]}");
                }})\n"""
            else:
                License += f"""\t\t$("#{framework}License{i+1}").load("/licenses/{packages[framework]["License"]["type"][i]}.html", function () {{
                    $("#{framework}License{i+1} a").attr("href", "{packages[framework]['License']['URL'][i]}");
                }})\n"""
    return License


def get_divLanguage(packages, framework) -> str:
    divLanguage = ""
    if len(packages[framework]["Language"]) == 1:
        divLanguage += f"""<div id="{framework}Language"></div>\n"""
    else:
        for i, _ in enumerate(packages[framework]["Language"]):
            if i == 0:
                divLanguage += f"""<div id="{framework}Language{i+1}"></div>\n"""
            else:
                divLanguage += f"""\t\t<div id="{framework}Language{i+1}"></div>\n"""
    return divLanguage


def get_divLicense(packages, framework) -> str:
    divLicense = ""
    if len(packages[framework]["License"]["type"]) == 1:
        divLicense += f"""<div id="{framework}License"></div>\n"""
    else:
        for i, _ in enumerate(packages[framework]["License"]):
            if i == 0:
                divLicense += f"""<div id="{framework}License{i+1}"></div>\n"""
            else:
                divLicense += f"""\t\t<div id="{framework}License{i+1}"></div>\n"""
    return divLicense


def get_divDevelopers(packages, framework) -> str:
    divDevelopers = ""
    if len(packages[framework]["Developers"]) == 1:
        divDevelopers += f"""
            <span class="selected-value select-value-color-{packages[framework]["Developers"][0]["color"]}">
                <a href="{packages[framework]["Developers"][0]["URL"]}" style="text-decoration: none">
                    {packages[framework]["Developers"][0]["name"]}
                </a>
            </span>
            """
    else:
        for i, _ in enumerate(packages[framework]["Developers"]):
            if i == 0:
                divDevelopers += f"""
                    <span class="selected-value select-value-color-{packages[framework]["Developers"][i]["color"]}">
                        <a href="{packages[framework]["Developers"][i]["URL"]}" style="text-decoration: none">
                            {packages[framework]["Developers"][i]["name"]}
                        </a>
                    </span>
                    """
            else:
                divDevelopers += f"""\t\t
                    <span class="selected-value select-value-color-{packages[framework]["Developers"][i]["color"]}">
                        <a href="{packages[framework]["Developers"][i]["URL"]}" style="text-decoration: none">
                            {packages[framework]["Developers"][i]["name"]}
                        </a>
                    </span>
                    """
    return divDevelopers


def get_divDocs(packages, framework) -> str:
    divDocs = ""
    if len(packages[framework]["Docs"]) == 1:
        divDocs += f"""
            <a href="{packages[framework]["Docs"][0]["URL"]}" class="url-value">
                {packages[framework]["Docs"][0]["link"]}
            </a>
            """
    else:
        for i, _ in enumerate(packages[framework]["Docs"]):
            if i == 0:
                divDocs += f"""
                    <a href="{packages[framework]["Docs"][i]["URL"]}" class="url-value">
                        {packages[framework]["Docs"][i]["link"]}
                    </a>
                    """
            else:
                divDocs += f"""\t\t
                    <a href="{packages[framework]["Docs"][i]["URL"]}" class="url-value">
                        {packages[framework]["Docs"][i]["link"]}
                    </a>
                    """
    return divDocs


def get_divSupport(packages, framework) -> str:
    divSupport = ""
    if len(packages[framework]["Support"]) == 1:
        divSupport += f"""
            <a href="{packages[framework]["Support"][0]["URL"]}" class="url-value">
                {packages[framework]["Support"][0]["link"]}
            </a>
            """
    else:
        for i, _ in enumerate(packages[framework]["Support"]):
            if i == 0:
                divSupport += f"""
                    <a href="{packages[framework]["Support"][i]["URL"]}" class="url-value">
                        {packages[framework]["Support"][i]["link"]}
                    </a>
                    """
            else:
                divSupport += f"""\t\t
                    <a href="{packages[framework]["Support"][i]["URL"]}" class="url-value">
                        {packages[framework]["Support"][i]["link"]}
                    </a>
                    """
    return divSupport


def generate_packages_load_MAIN(packages, framework) -> str:

    packages_load_MAIN = f"""
            // {framework}
            $("#{framework}").load("/packages/{framework}.html", function () {{
                {get_Language(packages, framework)}
                {get_License(packages, framework)}
            }});
        """
    return packages_load_MAIN


def genrete_HTML(packages, framework) -> str:

    package_HTML = f"""
        <!-- FRAMEWORK -->
        <td class="cell-framework">
            <a href="https://www.gpflow.org" style="text-decoration: none">
                <b> {framework} </b>
                <br style="margin-bottom: 8px" />
                
                <!-- REFERENCE -->
                <a href="{packages[framework]["Reference"]["URL"]}" style="text-decoration: none">
                    <i> {packages[framework]["Reference"]["Authors"]} </i>
                </a>
            </a>
        </td>

        <!-- LANGUAGE -->
        <td class="cell-language">
            {get_divLanguage(packages, framework)[:-1]}
        </td>

        <!-- LICENSE -->
        <td class="cell-license">
            {get_divLicense(packages, framework)[:-1]}
        </td>

        <!-- RELEASE -->
        <td class="cell-release">
            <a href="{packages[framework]['Release']['URL']}" style="text-decoration: none">
                {packages[framework]['Release']['version']}
            </a>
        </td>

        <!-- DEVELOPERS -->
        <td class="cell-dev">
            {get_divDevelopers(packages, framework)}
        </td>

        <!-- DOCS -->
        <td class="cell-documentation">
            {get_divDocs(packages, framework)}
        </td>

        <!-- SUPPORT -->
        <td class="cell-support">
            {get_divSupport(packages, framework)}
        </td>

        <!-- BASIS -->
        <td class="cell-basis"></td>

        <!-- KERNEL -->
        <td class="cell-kernel">
            <!-- <span class="selected-value select-value-color-purple">
                Isotropyic
            </span>
            <span class="selected-value select-value-color-yellow">
                Anisotrpic
            </span>  -->
        </td>

        <!-- CORRELATION -->
        <td class="cell-correlation">
            <!-- <span class="selected-value select-value-color-blue">
                Constant
            </span>
            <span class="selected-value select-value-color-brown">
                Squared Exponential
            </span>
            <span class="selected-value select-value-color-blue">
                Periodic
            </span>
            <span class="selected-value select-value-color-brown">
                Change Points
            </span>
            <span class="selected-value select-value-color-blue">
                Matérn
            </span>
            <span class="selected-value select-value-color-blue">
                Custom
            </span> -->
        </td>

        <!-- KERNEL MIXTURE -->
        <td class="cell-mixture" style="text-align: center">
            <div class="checkbox checkbox-on"></div>
        </td>

        <!-- OPTIMIZATION PROBLEM SOLVER -->
        <td class="cell-opt-problem">
            <span class="selected-value select-value-color-brown"> Exact </span>
        </td>

        <!-- OPTIMIZATION ALGORITHM -->
        <td class="cell-opt-algo"></td>
        """
    return package_HTML


def main() -> None:

    packages = pk.packages
    load_package, table_rows, style_package_hover, style_package_hover_child = "", "", "", ""
    for framework in sorted(packages.keys(), key=lambda x: x.lower()):

        package_HTML = genrete_HTML(packages, framework)
        with open(f"./packages_/{framework}.html", "w", encoding="UTF-8") as file:
            file.write(package_HTML)
        subprocess.run(["prettier", "--write", f"./packages_/{framework}.html"])  # pylint: disable=subprocess-run-check

        load_package += generate_packages_load_MAIN(packages, framework)
        table_rows += f"""<tr id="{framework}"></tr>\n"""
        style_package_hover += f"""#{framework}:hover,\n"""
        style_package_hover_child += f"""#{framework}:hover  td:first-child,\n"""

    loader = f"""
        <script>
            $(document).ready(function () {{
                {load_package}
            }});
        </script>
        """

    table_writer = f"""
        <tbody>
            {table_rows}
        </tbody>
    """

    style_writer = f"""
        {style_package_hover[:-2]}
        {{
            background-color: #f7fff1;
        }}\n
        {style_package_hover_child[:-2]}
        {{
            background-color: #f7fff1;
        }}
        """

    with open("./tmp/main_load.html", "w", encoding="UTF-8") as file:
        file.write(loader)

    with open("./tmp/main_table.html", "w", encoding="UTF-8") as file:
        file.write(table_writer)

    with open("./tmp/style_hover.css", "w", encoding="UTF-8") as file:
        file.write(style_writer)

    subprocess.run(["prettier", "--write", "./tmp/main_load.html"])  # pylint: disable=subprocess-run-check
    subprocess.run(["prettier", "--write", "./tmp/main_table.html"])  # pylint: disable=subprocess-run-check
    subprocess.run(["prettier", "--write", "./tmp/style_hover.css"])  # pylint: disable=subprocess-run-check

    print("Files created successfully.")


if __name__ == "__main__":
    main()
