from flask import Flask, render_template, request
import yaml, json, xmltodict

app = Flask(__name__)


def yaml_to_json(yamlstring):
    obj = yaml.safe_load(yamlstring)
    json_string = json.dumps(obj, indent=3)
    return json_string


def json_to_xml(s):
    s = json.loads(s)
    return xmltodict.unparse(s, pretty=True)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/', methods=['GET', 'POST'])
def publisher():
    if request.method == 'POST':
        details = request.form
        name = details['box1']
        # print(name)
    x = yaml_to_json(name)

    return render_template('home.html', x=x, a=name, y=json_to_xml(x))
