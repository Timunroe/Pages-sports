from jinja2 import Environment, FileSystemLoader
from string import Template
import htmlmin
import io
import script_templates as tmpl
import fetch
import model


# Put <script src="https://picabot.s3.amazonaws.com/pagejs/xxxx.js"></script> in DNN footer
# put <div class="pica-results"></div> in DNN body


def minify_html(s_html):
    # returns string of minified html
    return htmlmin.minify(s_html, remove_comments=True, remove_empty_space=True)


def save_file_overwrite(s_contents, s_file_name):
    print("++++++++++\nNow in save file module")
    build_directory = 'build'
    with io.open(f"{build_directory}/{s_file_name}", "w+", encoding='utf8') as file:
        file.write(s_contents)
    print(f"File saved in {build_directory}: {s_file_name}")
    return


def build_template(s_file_name):
    # NEED TO CREATE BUILD DIRECTORY IF IT DOESN'T EXIST!!!
    print("Building template for DNN")
    template_name = s_file_name + '.html'

    template_data = {"posts": model.get_lineup(filename)}
    # using Jinja2 string was fun, but let's get back to includes and other good stuff
    # html = Environment().from_string(tmpl.core_template).render(data=template_data)
    j2_env = Environment(loader=FileSystemLoader('templates'), trim_blocks=True)
    html = j2_env.get_template(template_name).render(data=template_data)
    html_minified = minify_html(html)
    css = fetch.fetch_css()
    script_name = s_file_name + '.js'
    script_template = getattr(tmpl, s_file_name)
    script = Template(script_template).substitute(css=css, minified=html_minified)
    # script = Template(tmpl.script_template).substitute(css=css, minified=html_minified)
    save_file_overwrite(script, script_name)
    pass


# if __name__ == "__main__":
    # call api, update database
    # model.get_new_data()
    # build template
    # build_template()
