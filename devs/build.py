# FILES GENERATOR

import subprocess
import packages.List as pk
import style.Basic as sty

def cleaner_string(input_string):
    return input_string.translate(str.maketrans("", "", "[] ."))

def get_Language(packages, framework) -> str:
    clean_name = cleaner_string(framework)
    languages = packages[framework]["Language"]
    language_lines = []
    for i, language in enumerate(languages):
        clean_language = cleaner_string(language)
        language_selector = (
            f"{clean_name}Language{i+1}" if len(languages) > 1 else f"{clean_name}Language"
        )
        line = f"""$("#{language_selector}").load("/languages/{clean_language}.html");"""
        language_lines.append(line)
    return "\n".join(language_lines)


def get_License(packages, framework) -> str:
    clean_framework = cleaner_string(framework)
    license_types = packages[framework]["License"]["type"]
    license_urls = packages[framework]["License"]["URL"]
    license_lines = []
    for i, license_type in enumerate(license_types):
        clean_license = cleaner_string(license_type)
        license_selector = (
            f"{clean_framework}License{i+1}"
            if len(license_types) > 1
            else f"{clean_framework}License"
        )
        license_url = license_urls[i]
        line = f"""$("#{license_selector}").load("/licenses/{clean_license}.html", function () {{\n"""
        line += f"""    $("#{license_selector} a").attr("href", "{license_url}");\n"""
        line += "})"
        license_lines.append(line)
    return "\n".join(license_lines)


def get_divLanguage(packages, framework) -> str:
    clean_framework = cleaner_string(framework)
    languages = packages[framework]["Language"]
    divs = []
    for i in range(len(languages)):
        div_id = f"{clean_framework}Language{i+1 if len(languages) > 1 else ''}"
        divs.append(f'<div id="{div_id}"></div>')
    return "\n".join(divs) + "\n"


def get_divLicense(packages, framework) -> str:
    clean_framework = cleaner_string(framework)
    license_count = len(packages[framework]["License"]["type"])
    divs = []
    for i in range(license_count):
        div_id = f"{clean_framework}License{i+1 if license_count > 1 else ''}"
        divs.append(f'<div id="{div_id}"></div>')
    return "\n".join(divs) + "\n"


def get_divDevelopers(packages, framework) -> str:
    developers = packages[framework]["Developers"]
    divs = []
    for developer in developers:
        div = f"""
            <span class="selected-value select-value-color-{developer["color"]}">
                <a href="{developer["URL"]}" style="text-decoration: none">
                    {developer["name"]}
                </a>
            </span>
        """
        divs.append(div)
    return "\n".join(divs).strip()


def get_divDocs(packages, framework) -> str:
    docs = packages[framework]["Docs"]
    spans = [
        f"""<span class="selected-value select-value-color-{doc["color"]}">
        <a href="{doc["URL"]}" style="text-decoration: none">{doc["link"]}</a></span>"""
        for doc in docs
    ]
    return "\n".join(spans)


def get_divSupport(packages, framework) -> str:
    support_items = packages[framework]["Support"]
    spans = [
        f"""<span class="selected-value select-value-color-{support["color"]}">
        <a href="{support["URL"]}" style="text-decoration: none">{support["link"]}</a></span>"""
        for support in support_items
    ]
    return "\n".join(spans)


def generate_packages_load_MAIN(packages, framework) -> str:
    clean_framework = cleaner_string(framework)
    packages_load_MAIN = f"""
    \n\n// {framework}
    $("#{clean_framework}").load("/packages/{clean_framework}.html", function () {{
        {get_Language(packages, framework)}
        {get_License(packages, framework)}
    }});
    """
    return packages_load_MAIN


def generate_HTML(packages, framework) -> str:
    package_HTML = f"""
        <!-- FRAMEWORK -->
        <td class="cell-framework">
            <a href="{packages[framework]["URL"]}" style="text-decoration: none">
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
            <a href="{packages[framework]['Release']['URL']}" class="version" style="text-decoration: none">
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

def generate_main_HTML(script, tbody) -> str:

    main = f"""
    <html style="width: 2600px !important;">
    <!-- HEAD -->
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        {script}
        <title>
            A comprehensive guide to Kriging metamodeling toolboxes
        </title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <!-- BODY -->
    <body>
        <article id="Article" class="page sans">
            <header style="width: 400px !important; height: 100px !important;">
                <!-- TABLE TITLE -->
                <h1 class="page-title" style="width: 1100px !important;">
                    A comprehensive guide to Kriging metamodeling toolboxes</h1>
            </header>
            <div class="page-body" style="width: 1000px !important;">
                <!-- SEARCHER -->
                <label>
                    <input type="text" id="searchInput" placeholder="Press ⌘ / ⌃ + K to search">
                </label>
                <!-- BUTTON -->
                <button id="filterC" class="select-filter-c">C</button>
                <button id="filterCpp" class="select-filter-cpp">C++</button>
                <button id="filterGo" class="select-filter-go">GO</button>
                <button id="filterJulia" class="select-filter-julia">julia</button>
                <button id="filterMatlab" class="select-filter-matlab">MATLAB</button>
                <button id="filterOctave" class="select-filter-octave">GNU Octave</button>
                <button id="filterPython" class="select-filter-python">Python</button>
                <button id="filterR" class="select-filter-r">R</button>
                <button id="filterRust" class="select-filter-rust">Rust</button>
                <!-- TABLE -->
                <table id="myTable" class="collection-content">
                    <!-- TABLE HEADER -->
                    <thead>
                        <tr>
                            <th style="min-width: 9em; position: sticky;">FRAMEWORK</th>
                            <th style="min-width: 4.5em;">LANGUAGE</th>
                            <th>LICENSE</th>
                            <th>RELEASE</th>
                            <th style="min-width: 14.5em;">DEVELOPERS & FUNDING</th>
                            <th style="min-width: 6.5em;">DOCUMENTATION</th>
                            <th style="min-width: 21em;">COMMUNITY SUPPORT & DISCUSSIONS</th>
                            <th>TREND TYPES</th>
                            <th>KERNEL</th>
                            <th style="min-width: 19.5em;">KERNEL FAMILIES &nbsp \\( R(x,x';\\theta) \\)</th>
                            <th style="min-width: 9.5em;">KERNEL MIXTURE</th>
                            <th>SOLVER</th>
                            <th style="min-width: 14.5em;">OPTIMIZATION ALGORITHM</th>
                        </tr>
                    </thead>
                    <!-- TABLE BODY ORDINE ALFABETICO -->
                    {tbody}
                    </table>
                    <br>
                    <!-- FOOTER -->

                    <p style="font-size: 9pt !important; color:#9ca2a8; margin-top: -15px !important; width:2000px !important;">
                        <i>Source: © A. Faraci, P. Beaurepaire, N. Gayton; A comprehensive guide to Kriging metamodeling
                            toolboxes: bridging theory with practice through features, limitations, and performance.
                        </i>
                    </p>
                    <p style="font-size: 9pt !important; color:#9ca2a8; margin-top: -1px !important; width:2000px !important;">
                        <a
                            href="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en"
                            class = "link-style"
                            style="text-decoration: none; font-style: italic;"
                        >
                        This Project has received funding from the European Union’s Horizon 2020 research and innovation
                        programme under Marie Sklodowska-Curie project GREYDIENT – Grant Agreement n°955393
                        </a>
                    </p>
                    <br /><br />
                </div>
                </article>
                <span class="sans" style="font-size: 14px; padding-top: 2em"></span>
                """
    main +="""
            <!-- SCRIPTS -->
            <script>
            document.addEventListener('DOMContentLoaded', function () {
                // Event listener for search input to filter table rows
                document.getElementById('searchInput').addEventListener('keyup', function () {
                    var searchQuery = this.value.toLowerCase();
                    var table = document.getElementById('myTable');
                    var tableRows = table.getElementsByTagName('tr');

                    for (var i = 1; i < tableRows.length; i++) { // Starting from 1 to skip the header row
                        var cells = tableRows[i].getElementsByTagName('td');
                        var rowText = Array.from(cells).map(cell => cell.textContent.toLowerCase()).join(' ');
                        var displayStyle = rowText.indexOf(searchQuery) > -1 ? '' : 'none';

                        tableRows[i].style.display = displayStyle;
                    }
                });

                // Event listener for document to capture "Cmd+K" or "Ctrl+K"
                document.addEventListener('keydown', function (e) {
                    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                        e.preventDefault(); // Prevent the default action to ensure the shortcut works as intended
                        document.getElementById('searchInput').focus(); // Focus the search input
                    }
                });
            });
            </script>
            <script>
            document.addEventListener("DOMContentLoaded", function () {
                var input = document.getElementById('searchInput');
                if (navigator.platform.startsWith('Win')) {
                    input.placeholder = "Press ⌃ CTRL + K to search";
                } else if (navigator.platform.startsWith('Linux')) {
                    input.placeholder = "Press ⌃ CTRL + K to search";
                } else if (navigator.platform.startsWith('Mac')) {
                    input.placeholder = "Press ⌘ + K to search";
                } else {
                    // Default or unknown OS
                    input.placeholder = "Press ⌘ / ⌃ + K to search";
                }
            });
            </script>
            <script>
            document.addEventListener('DOMContentLoaded', function () {
                var table = document.getElementById('myTable');
                var lastFilter = '';

                function filterTableLanguage(filter) {
                    var tableRows = table.getElementsByTagName('tr');
                    var isFilterActive = lastFilter.toLowerCase() === filter.toLowerCase();

                    for (var i = 1; i < tableRows.length; i++) { // Assuming the first row is the header
                        // Target only the second column (index 1) of the current row
                        var cellText = tableRows[i].cells[1].textContent.toLowerCase();
                        if (!isFilterActive && filter !== '') {
                            var displayStyle = cellText.indexOf(filter.toLowerCase()) > -1 ? '' : 'none';
                            tableRows[i].style.display = displayStyle;
                        } else {
                            tableRows[i].style.display = '';
                        }
                    }
                    lastFilter = isFilterActive ? '' : filter; // Toggle the last filter
                }

                document.getElementById('filterC').addEventListener('click', function () {
                    filterTableLanguage('C ');
                });

                document.getElementById('filterCpp').addEventListener('click', function () {
                    filterTableLanguage('C++');
                });

                document.getElementById('filterGo').addEventListener('click', function () {
                    filterTableLanguage('Go');
                });

                document.getElementById('filterJulia').addEventListener('click', function () {
                    filterTableLanguage('Julia');
                });

                document.getElementById('filterMatlab').addEventListener('click', function () {
                    filterTableLanguage('Matlab');
                });

                document.getElementById('filterOctave').addEventListener('click', function () {
                    filterTableLanguage('Octave');
                });

                document.getElementById('filterPython').addEventListener('click', function () {
                    filterTableLanguage('Python');
                });

                document.getElementById('filterR').addEventListener('click', function () {
                    filterTableLanguage('R ');
                });

                document.getElementById('filterRust').addEventListener('click', function () {
                    filterTableLanguage('Rust');
                });

                // Optional: Clear the filter when the search input is modified
                document.getElementById('searchInput').addEventListener('keyup', function () {
                    // Clear the last filter when the user types in the search
                    lastFilter = '';
                    // Existing search functionality here...
                });
                // Rest of your search functionality...
            });
            </script>

            </body>

            </html>
            """
    return main

def generate_Table_HTML(script, tbody, style) -> str:

    main = f"""
    <html style="width: 2600px !important;">
    <!-- HEAD -->
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        {script}
        <title>
            A comprehensive guide to Kriging metamodeling toolboxes
        </title>
        <style>
        {style}
        </style>
    </head>
    <!-- BODY -->
    <body>
        <article id="Article" class="page sans">
            <header style="width: 400px !important; height: 100px !important;">
                <!-- TABLE TITLE -->
                <h1 class="page-title" style="width: 1100px !important;">
                    A comprehensive guide to Kriging metamodeling toolboxes</h1>
            </header>
            <div class="page-body" style="width: 1000px !important;">
                <!-- SEARCHER -->
                <label>
                    <input type="text" id="searchInput" placeholder="Press ⌘ / ⌃ + K to search">
                </label>
                <!-- BUTTON -->
                <button id="filterC" class="select-filter-c">C</button>
                <button id="filterCpp" class="select-filter-cpp">C++</button>
                <button id="filterGo" class="select-filter-go">GO</button>
                <button id="filterJulia" class="select-filter-julia">julia</button>
                <button id="filterMatlab" class="select-filter-matlab">MATLAB</button>
                <button id="filterOctave" class="select-filter-octave">GNU Octave</button>
                <button id="filterPython" class="select-filter-python">Python</button>
                <button id="filterR" class="select-filter-r">R</button>
                <button id="filterRust" class="select-filter-rust">Rust</button>
                <!-- TABLE -->
                <table id="myTable" class="collection-content">
                    <!-- TABLE HEADER -->
                    <thead>
                        <tr>
                            <th style="min-width: 9em; position: sticky;">FRAMEWORK</th>
                            <th style="min-width: 4.5em;">LANGUAGE</th>
                            <th>LICENSE</th>
                            <th>RELEASE</th>
                            <th style="min-width: 14.5em;">DEVELOPERS & FUNDING</th>
                            <th style="min-width: 6.5em;">DOCUMENTATION</th>
                            <th style="min-width: 21em;">COMMUNITY SUPPORT & DISCUSSIONS</th>
                            <th>TREND TYPES</th>
                            <th>KERNEL</th>
                            <th style="min-width: 19.5em;">KERNEL FAMILIES &nbsp \\( R(x,x';\\theta) \\)</th>
                            <th style="min-width: 9.5em;">KERNEL MIXTURE</th>
                            <th>SOLVER</th>
                            <th style="min-width: 14.5em;">OPTIMIZATION ALGORITHM</th>
                        </tr>
                    </thead>
                    <!-- TABLE BODY ORDINE ALFABETICO -->
                    {tbody}
                    </table>
                    <br>
                    <!-- FOOTER -->

                    <p style="font-size: 9pt !important; color:#9ca2a8; margin-top: -15px !important; width:2000px !important;">
                        <i>Source: © A. Faraci, P. Beaurepaire, N. Gayton; A comprehensive guide to Kriging metamodeling
                            toolboxes: bridging theory with practice through features, limitations, and performance.
                        </i>
                    </p>
                    <p style="font-size: 9pt !important; color:#9ca2a8; margin-top: -1px !important; width:2000px !important;">
                        <a
                            href="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en"
                            class = "link-style"
                            style="text-decoration: none; font-style: italic;"
                        >
                        This Project has received funding from the European Union’s Horizon 2020 research and innovation
                        programme under Marie Sklodowska-Curie project GREYDIENT – Grant Agreement n°955393
                        </a>
                    </p>
                    <br /><br />
                </div>
                </article>
                <span class="sans" style="font-size: 14px; padding-top: 2em"></span>
                """
    main +="""
            <!-- SCRIPTS -->
            <script>
            document.addEventListener('DOMContentLoaded', function () {
                // Event listener for search input to filter table rows
                document.getElementById('searchInput').addEventListener('keyup', function () {
                    var searchQuery = this.value.toLowerCase();
                    var table = document.getElementById('myTable');
                    var tableRows = table.getElementsByTagName('tr');

                    for (var i = 1; i < tableRows.length; i++) { // Starting from 1 to skip the header row
                        var cells = tableRows[i].getElementsByTagName('td');
                        var rowText = Array.from(cells).map(cell => cell.textContent.toLowerCase()).join(' ');
                        var displayStyle = rowText.indexOf(searchQuery) > -1 ? '' : 'none';

                        tableRows[i].style.display = displayStyle;
                    }
                });

                // Event listener for document to capture "Cmd+K" or "Ctrl+K"
                document.addEventListener('keydown', function (e) {
                    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                        e.preventDefault(); // Prevent the default action to ensure the shortcut works as intended
                        document.getElementById('searchInput').focus(); // Focus the search input
                    }
                });
            });
            </script>
            <script>
            document.addEventListener("DOMContentLoaded", function () {
                var input = document.getElementById('searchInput');
                if (navigator.platform.startsWith('Win')) {
                    input.placeholder = "Press ⌃ CTRL + K to search";
                } else if (navigator.platform.startsWith('Linux')) {
                    input.placeholder = "Press ⌃ CTRL + K to search";
                } else if (navigator.platform.startsWith('Mac')) {
                    input.placeholder = "Press ⌘ + K to search";
                } else {
                    // Default or unknown OS
                    input.placeholder = "Press ⌘ / ⌃ + K to search";
                }
            });
            </script>
            <script>
            document.addEventListener('DOMContentLoaded', function () {
                var table = document.getElementById('myTable');
                var lastFilter = '';

                function filterTableLanguage(filter) {
                    var tableRows = table.getElementsByTagName('tr');
                    var isFilterActive = lastFilter.toLowerCase() === filter.toLowerCase();

                    for (var i = 1; i < tableRows.length; i++) { // Assuming the first row is the header
                        // Target only the second column (index 1) of the current row
                        var cellText = tableRows[i].cells[1].textContent.toLowerCase();
                        if (!isFilterActive && filter !== '') {
                            var displayStyle = cellText.indexOf(filter.toLowerCase()) > -1 ? '' : 'none';
                            tableRows[i].style.display = displayStyle;
                        } else {
                            tableRows[i].style.display = '';
                        }
                    }
                    lastFilter = isFilterActive ? '' : filter; // Toggle the last filter
                }

                document.getElementById('filterC').addEventListener('click', function () {
                    filterTableLanguage('C ');
                });

                document.getElementById('filterCpp').addEventListener('click', function () {
                    filterTableLanguage('C++');
                });

                document.getElementById('filterGo').addEventListener('click', function () {
                    filterTableLanguage('Go');
                });

                document.getElementById('filterJulia').addEventListener('click', function () {
                    filterTableLanguage('Julia');
                });

                document.getElementById('filterMatlab').addEventListener('click', function () {
                    filterTableLanguage('Matlab');
                });

                document.getElementById('filterOctave').addEventListener('click', function () {
                    filterTableLanguage('Octave');
                });

                document.getElementById('filterPython').addEventListener('click', function () {
                    filterTableLanguage('Python');
                });

                document.getElementById('filterR').addEventListener('click', function () {
                    filterTableLanguage('R ');
                });

                document.getElementById('filterRust').addEventListener('click', function () {
                    filterTableLanguage('Rust');
                });

                // Optional: Clear the filter when the search input is modified
                document.getElementById('searchInput').addEventListener('keyup', function () {
                    // Clear the last filter when the user types in the search
                    lastFilter = '';
                    // Existing search functionality here...
                });
                // Rest of your search functionality...
            });
            </script>

            </body>

            </html>
            """
    return main

def main() -> None:
    packages = pk.packages
    load_package, table_rows, style_package_hover = "", "", ""

    for framework in sorted(packages.keys(), key=lambda x: x.lower()):
        clean_framework = cleaner_string(framework)
        package_HTML = generate_HTML(packages, framework)

        # Write the generated HTML for each package
        html_file_path = f"./packages/{clean_framework}.html"
        with open(html_file_path, "w", encoding="UTF-8") as file:
            file.write(package_HTML)
        subprocess.run(["prettier", "--write", "--tab-width", "4", html_file_path])

        # Accumulate strings for script, table rows, and style
        load_package += generate_packages_load_MAIN(packages, framework)
        table_rows += f'<tr id="{clean_framework}"></tr>\n'
        style_package_hover += f'#{clean_framework}:hover, #{clean_framework}:hover td:first-child,\n'

    script = f"""
    <script>
        $(document).ready(function () {{
            {load_package}
        }});
    </script>
    """

    tbody = f"""
    <tbody>
        {table_rows}
    </tbody>
    """

    style = sty.style
    style += f"""
    {style_package_hover.rstrip(',\n')}
    {{
        background-color: #f7fff1;
    }}
    """

    # Write final strings to files and format with prettier
    files_content = {
        "./main.html": generate_main_HTML(tbody=tbody, script=script),
        "./style.css": style,
        "../Table.html": generate_Table_HTML(tbody=tbody, script=script, style=style),
    }

    for file_path, content in files_content.items():
        with open(file_path, "w", encoding="UTF-8") as file:
            file.write(content)
        subprocess.run(["prettier", "--write", "--tab-width", "4", file_path])

    print("Files created successfully.")


if __name__ == "__main__":
    main()
