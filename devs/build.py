# FILES GENERATOR

import subprocess
import utils.list as pkg
import utils.basic as sty


def cleaner_string(input_string):
    return input_string.translate(str.maketrans("", "", "[] . /"))


def get_Language(packages, framework) -> str:
    clean_name = cleaner_string(framework)
    languages = packages[framework]["Language"]
    language_lines = []
    for i, language in enumerate(languages):
        clean_language = cleaner_string(language)
        language_selector = f"{clean_name}Language{i+1}" if len(languages) > 1 else f"{clean_name}Language"
        line = f"""$("#{language_selector}").load("/languages/{clean_language}.html");"""
        language_lines.append(line)
    return "\n".join(language_lines)


def get_License(packages, framework) -> str:
    clean_framework = cleaner_string(framework)
    license_types = packages[framework]["License"]["type"]
    license_urls = [url if url != "" else "javascript:void(0);" for url in packages[framework]["License"].get("URL", [])]
    license_lines = []
    for i, license_type in enumerate(license_types):
        clean_license = cleaner_string(license_type)
        license_selector = f"{clean_framework}License{i+1}" if len(license_types) > 1 else f"{clean_framework}License"
        line = f"""$("#{license_selector}").load("/licenses/{clean_license}.html", function () {{\n"""
        line += f"""    $("#{license_selector} a").attr("href", "{license_urls[i]}");\n"""
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
    color = {
        "docs": "default",
        "py docs": "default",
        "jl docs": "default",
        "r docs": "default",
        "mat docs": "default",
        "user manuals": "blue",
        "examples": "green",
        "py examples": "green",
        "jl examples": "green",
        "R examples": "green",
        "mat examples": "green",
        "tutorials": "purple",
        "jupyter notebooks": "orange",
        "colab cookbook": "orange",
        "API": "yellow",
        "py API": "yellow",
        "jl API": "yellow",
        "r API": "yellow",
        "mat API": "yellow",
        "talk": "red",
    }
    spans = [
        f"""<span class="selected-value select-value-color-{color.get(doc["tag"], 'default')}">
        <a href="{doc["URL"]}" style="text-decoration: none">{doc["tag"]}</a></span>"""
        for doc in docs
    ]
    return "\n".join(spans)


def get_divBaseFramework(packages, framework_) -> str:
    baseFramework = packages[framework_]["Framework"]
    color = {
        "PyTorch": "purple",
        "TensorFlow": "orange",
        "Keras": "red",
        "JAX": "teal",
        "numpy": "blue",
    }
    spans = [
        f"""<span class="selected-value select-value-color-{color.get(frame["tag"], 'default')}">
        <a href="{frame["URL"]}" style="text-decoration: none">{frame["tag"]}</a></span>"""
        for frame in baseFramework
    ]
    return "\n".join(spans)


def get_divGPU(packages, framework) -> str:
    if packages[framework]["GPU"]:
        return '<div class="checkbox checkbox-on"></div>'
    else:
        return '<div class="checkbox checkbox-off"></div>'


def get_divMixture(packages, framework) -> str:
    if packages[framework]["Kernel"]["Mixture"]["check"]:
        return '<div class="checkbox checkbox-on"></div>'
    else:
        return '<div class="checkbox checkbox-off"></div>'


def get_divSupport(packages, framework) -> str:
    support_items = packages[framework]["Support"]
    color = {
        "slack": "orange",
        "stackoverflow": "yellow",
        "contact form": "blue",
        "mailing-list": "blue",
        "forum": "green",
        "blog": "pink",
        "chat": "purple",
        "GitHub discussions": "default",
    }
    spans = [
        f"""<span class="selected-value select-value-color-{color.get(support["tag"], 'default')}">
        <a href="{support["URL"]}" style="text-decoration: none">{support["tag"]}</a></span>"""
        for support in support_items
    ]
    return "\n".join(spans)


def get_divLengthScale(packages, framework) -> str:
    lenScale_items = packages[framework]["Kernel"]["LengthScale"]
    color = {
        "Isotropic": "purple",
        "Anisotropic": "yellow",
    }
    spans = [
        f"""<span class="selected-value select-value-color-{color.get(lenScale, 'default')}">
            {lenScale}</span>"""
        for lenScale in lenScale_items
    ]
    return "\n".join(spans)


def get_divTrend(packages, framework) -> str:
    trend_items = packages[framework]["Trend"]["tag"]
    color = {
        "Zero": "green",
        "Constant": "blue",
    }
    spans = [
        f"""<a href="{packages[framework]["Trend"].get("URL", "javascript:void(0);") or "javascript:void(0);"}" style="text-decoration: none">
            <span class="selected-value select-value-color-{color.get(trend, 'default')}">
            {trend}</span></a>"""
        for trend in trend_items
    ]
    return "\n".join(spans)


def get_divFamilies(packages, framework) -> str:
    families_items = packages[framework]["Kernel"]["Families"]["tag"]
    color = {
        "Constant": "blue",
        "Linear": "yellow",
    }
    spans = [
        f"""<a href="{packages[framework]["Kernel"]["Families"].get("URL", "javascript:void(0);") or "javascript:void(0);"}" style="text-decoration: none">
            <span class="selected-value select-value-color-{color.get(family, 'default')}">
            {family}</span></a>"""
        for family in families_items
    ]
    return "\n".join(spans)


def get_divMixutureModels(packages, framework) -> str:
    models_items = packages[framework]["Kernel"]["Mixture"]["tag"]
    color = {
        "Sum": "blue",
        "Product": "yellow",
    }
    spans = [
        f"""<a href="{packages[framework]["Kernel"]["Mixture"].get("URL", "javascript:void(0);") or "javascript:void(0);"}" style="text-decoration: none">
            <span class="selected-value select-value-color-{color.get(model, 'default')}">
            {model}</span></a>"""
        for model in models_items
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
        <!-- LIBRARY -->
        <td class="cell-library">
            <a href="{packages[framework]["URL"]}" style="text-decoration: none">
                <b> {framework} </b>
                <br style="margin-bottom: 8px" />

                <!-- REFERENCE -->
                <a href="{packages[framework]["Reference"].get("URL", "javascript:void(0);") or "javascript:void(0);"}" style="text-decoration: none">
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
            <a href="{packages[framework]["Release"].get("URL", "javascript:void(0);") or "javascript:void(0);"}" class="version" style="text-decoration: none">
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

        <!-- FRAMEWORK -->
        <td class="cell-framework">
            {get_divBaseFramework(packages, framework)}
        </td>

        <!-- GPU -->
        <td class="cell-gpu" style="text-align: center">
            {get_divGPU(packages, framework)}
        </td>

        <!-- BASIS -->
        <td class="cell-basis">
            {get_divTrend(packages, framework)}
        </td>

        <!-- LENGTH SCALE -->
        <td class="cell-lengthscale">
            {get_divLengthScale(packages, framework)}
        </td>

        <!-- CORRELATION -->
        <td class="cell-correlation">
            {get_divFamilies(packages, framework)}
        </td>

        <!-- KERNEL MIXTURE -->
        <td class="cell-mixture" style="text-align: center">
            {get_divMixture(packages, framework)}
        </td>

        <!-- MIXTURE MODEL -->
        <td class="cell-mixture-model">
            {get_divMixutureModels(packages, framework)}
        </td>

        <!-- ESTIMATION METHODS -->
        <td class="cell-estimation"></td>

        <!-- OPTIMIZATION ALGORITHM -->
        <td class="cell-opt-algo"></td>

        <!-- N RESTART -->
        <td class="cell-opt-restart"></td>

        <!-- NUGGET -->
        <td class="cell-opt-nugget"></td>
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
            A comprehensive guide to Gaussian Process Regression libraries
        </title>
        <link rel="stylesheet" type="text/css" href="style.css">
    </head>
    <!-- BODY -->
    <body>
        <article id="Article" class="page sans">
            <header style="width: 400px !important; height: 100px !important;">
                <!-- TABLE TITLE -->
                <h1 class="page-title" style="width: 1200px !important;">
                    A comprehensive guide to Gaussian Process Regression libraries</h1>
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

                            <th rowspan="2"
                                style="min-width: 166px !important;">
                                LIBRARY
                            </th>

                            <th rowspan="2"
                                style="min-width: 121px !important;">
                                LANGUAGE
                            </th>

                            <th rowspan="2"
                                style="min-width: 129px !important;">
                                LICENSE
                            </th>

                            <th rowspan="2"
                                style="min-width: 120px !important;">
                                RELEASE
                            </th>

                            <th rowspan="2"
                                style="min-width: 14.5em;">
                                DEVELOPERS & FUNDING
                            </th>

                            <th rowspan="2"
                                style="min-width: 6.5em;">
                                DOCUMENTATION
                            </th>

                            <th rowspan="2"
                                style="min-width: 175px !important;">
                                COMMUNITY SUPPORT
                            </th>

                            <th rowspan="2">
                                FRAMEWORK
                            </th>

                            <th rowspan="2"
                                style="text-align: center">
                                GPU ACCELERATION
                            </th>

                            <th rowspan="2"
                                style="min-width: 122px !important;">
                                TREND TYPES
                            </th>

                            <th colspan="4"
                                style="text-align: center">
                                KERNEL  &nbsp \\( R(x,x';\\theta) \\)
                            </th>

                            <th rowspan="2">
                                ESTIMATION METHODS
                            </th>

                            <th colspan="3"
                                style="min-width: 14.5em;"
                                style="text-align: center">
                                OPTIMIZATION METHODS
                            </th>
                        </tr>

                        <!-- SECOND ROW -->
                        <tr class="second-row">

                            <th style="min-width: 120px !important;">
                                LENGTH SCALE
                            </th>

                            <th style="min-width: 175px !important;">
                                CORRELATION FAMILIES
                            </th>

                            <th>
                                MIXTURE
                            </th>

                            <th style="min-width: 140px !important;">
                                MIXTURE MODEL
                            </th>

                            <th style="min-width: 9.5em;">
                                ALGORITHMS
                            </th>

                            <th style="min-width: 9.5em;">
                                N. RESTARTS
                            </th>

                            <th style="min-width: 9.5em;">
                                NUGGET
                            </th>

                        </tr>
                    </thead>
                    <!-- TABLE BODY ORDINE ALFABETICO -->
                    {tbody}
                    </table>
                    <br>
                    <!-- FOOTER -->

                    <p style="font-size: 9pt !important; color:#9ca2a8; margin-top: -15px !important; width:2000px !important;">
                        <i>Source: © A. Faraci, P. Beaurepaire, N. Gayton; A comprehensive guide to Gaussian Process Regression
                            libraries: bridging theory with practice through features, limitations, and performance.
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
    main += """
            <!-- SCRIPTS -->
            <script>
                document.addEventListener("DOMContentLoaded", function () {
                    var table = document.getElementById("myTable");
                    var input = document.getElementById("searchInput");
                    var lastFilter = "";

                    // Function to update row colors
                    function updateRowColors() {
                        var tableRows = table.getElementsByTagName("tr");
                        var visibleRowIndex = 0;
                        for (var i = 2; i < tableRows.length; i++) {
                            if (tableRows[i].style.display !== "none") {
                                tableRows[i].style.backgroundColor =
                                    visibleRowIndex % 2 === 0
                                        ? "#ffffff"
                                        : "#f6f8fa";
                                visibleRowIndex++;
                            }
                        }
                    }

                    // Search functionality
                    input.addEventListener("keyup", function () {
                        var searchQuery = this.value.toLowerCase();
                        var tableRows = table.getElementsByTagName("tr");

                        for (var i = 2; i < tableRows.length; i++) {
                            var cells = tableRows[i].getElementsByTagName("td");
                            var rowText = Array.from(cells)
                                .map((cell) => cell.textContent.toLowerCase())
                                .join(" ");
                            tableRows[i].style.display =
                                rowText.indexOf(searchQuery) > -1 ? "" : "none";
                        }
                        lastFilter = ""; // Reset filter
                        updateRowColors();
                    });

                    // Filter functionality
                    function filterTableLanguage(filter) {
                        var tableRows = table.getElementsByTagName("tr");
                        var isFilterActive =
                            lastFilter.toLowerCase() === filter.toLowerCase();

                        for (var i = 2; i < tableRows.length; i++) {
                            // Check if the filter is active or if a specific filter should be applied
                            if (!isFilterActive && filter !== "") {
                                var cellText =
                                    tableRows[i].cells[1].textContent.toLowerCase();
                                var shouldDisplay =
                                    cellText.indexOf(filter.toLowerCase()) > -1;
                                tableRows[i].style.display = shouldDisplay
                                    ? ""
                                    : "none";
                            } else {
                                // If the filter is currently active, or no specific filter is applied, reset to show all rows
                                tableRows[i].style.display = "";
                            }
                        }

                        // Toggle the lastFilter value: if the filter is active, clear it, otherwise set it to the current filter
                        lastFilter = isFilterActive ? "" : filter;
                        updateRowColors();
                    }

                    // Filter buttons
                    document
                        .getElementById("filterC")
                        .addEventListener("click", function () {
                            filterTableLanguage("C ");
                        });

                    document
                        .getElementById("filterCpp")
                        .addEventListener("click", function () {
                            filterTableLanguage("C++");
                        });

                    document
                        .getElementById("filterGo")
                        .addEventListener("click", function () {
                            filterTableLanguage("Go");
                        });

                    document
                        .getElementById("filterJulia")
                        .addEventListener("click", function () {
                            filterTableLanguage("Julia");
                        });

                    document
                        .getElementById("filterMatlab")
                        .addEventListener("click", function () {
                            filterTableLanguage("Matlab");
                        });

                    document
                        .getElementById("filterOctave")
                        .addEventListener("click", function () {
                            filterTableLanguage("Octave");
                        });

                    document
                        .getElementById("filterPython")
                        .addEventListener("click", function () {
                            filterTableLanguage("Python");
                        });

                    document
                        .getElementById("filterR")
                        .addEventListener("click", function () {
                            filterTableLanguage("R ");
                        });

                    document
                        .getElementById("filterRust")
                        .addEventListener("click", function () {
                            filterTableLanguage("Rust");
                        });

                    // Keyboard shortcut functionality
                    document.addEventListener("keydown", function (e) {
                        if ((e.metaKey || e.ctrlKey) && e.key === "k") {
                            e.preventDefault();
                            input.focus();
                        }
                    });

                    // Placeholder text based on OS
                    if (
                        navigator.platform.startsWith("Win") ||
                        navigator.platform.startsWith("Linux")
                    ) {
                        input.placeholder = "Press ⌃ CTRL + K to search";
                    } else if (navigator.platform.startsWith("Mac")) {
                        input.placeholder = "Press ⌘ + K to search";
                    } else {
                        input.placeholder = "Press ⌘ / ⌃ + K to search";
                    }
                });
            </script>
            </body>
            </html>
            """
    return main


def main() -> None:
    packages = pkg.packages
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
        style_package_hover += f"#{clean_framework}:hover, #{clean_framework}:hover td:first-child,\n"

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
    # {style_package_hover.rstrip(',\n')}
    style += f"""
    {style_package_hover}
    {{
        background-color: #f7fff1;
    }}
    """

    # Write final strings to files and format with prettier
    files_content = {
        "./main.html": generate_main_HTML(tbody=tbody, script=script),
        "./style.css": style,
        # "../Table.html": generate_Table_HTML(tbody=tbody, script=script, style=style),
    }

    for file_path, content in files_content.items():
        with open(file_path, "w", encoding="UTF-8") as file:
            file.write(content)
        subprocess.run(["prettier", "--write", "--tab-width", "4", file_path])

    print("Files created successfully.")


if __name__ == "__main__":
    main()

    # AppleScript command
    applescript_command = """
    tell application "Safari"
        set targetURL to "http://localhost:8000/main.html"
        repeat with win in windows
            repeat with t in tabs of win
                if URL of t is targetURL then
                    tell t to do JavaScript "window.location.reload()"
                    exit repeat
                end if
            end repeat
        end repeat
    end tell
    """

    # Execute the AppleScript command from Python
    subprocess.run(["osascript", "-e", applescript_command])
