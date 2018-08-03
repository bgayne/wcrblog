from flask import Flask, send_file, send_from_directory, render_template
from flask import request, Response, jsonify
from flask import send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

lorems = '''
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ex, ducimus necessitatibus earum quae officia impedit, molestias magni culpa ipsum labore provident! Aliquam itaque corrupti numquam impedit quam molestias eos! Suscipit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nostrum, accusantium? Nemo quasi, officiis accusantium porro unde reprehenderit necessitatibus illum quos reiciendis at fuga vel iste sequi dolores ullam hic nisi? Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam debitis nulla maxime deserunt illo explicabo dolor praesentium dignissimos veritatis dolore officiis cum omnis nihil, optio vitae modi officia rerum aspernatur!
                <br>
                <br>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate aliquam praesentium, velit quidem nostrum, facere dicta fuga nobis hic odit aut ullam excepturi culpa sunt consequuntur assumenda pariatur, debitis numquam! Lorem ipsum, dolor sit amet consectetur adipisicing elit. Corporis neque explicabo iusto! Laborum veritatis asperiores nostrum dolorem eligendi illo ducimus, architecto, sed pariatur tempora porro distinctio, incidunt illum deserunt delectus. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Debitis adipisci fugit sapiente, sit maiores soluta culpa nesciunt quam provident illo non vitae minima eligendi enim nisi dignissimos fuga, id molestiae!
                <br>
                <br>
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Non quae molestiae ad libero, voluptate delectus illum debitis. Debitis, sunt minus eos alias quo dolores enim est eius, porro sit totam. Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis aut nam, optio unde, odio architecto tempora expedita fugit ipsa in, earum doloremque fugiat cumque praesentium nesciunt pariatur delectus obcaecati? Consequatur! Lorem ipsum, dolor sit amet consectetur adipisicing elit. Omnis tempora voluptas quidem rerum alias est, maxime quasi, ipsa eum officia nostrum sequi nisi incidunt impedit, officiis ratione. Quo, eius quibusdam? Lorem ipsum dolor sit amet consectetur, adipisicing elit. Veniam incidunt quo eveniet error ullam ab, animi blanditiis quis recusandae corrupti sequi illum quisquam praesentium iusto natus ratione provident excepturi obcaecati.
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ex, ducimus necessitatibus earum quae officia impedit, molestias magni culpa ipsum labore provident! Aliquam itaque corrupti numquam impedit quam molestias eos! Suscipit. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Nostrum, accusantium? Nemo quasi, officiis accusantium porro unde reprehenderit necessitatibus illum quos reiciendis at fuga vel iste sequi dolores ullam hic nisi? Lorem ipsum dolor sit amet consectetur adipisicing elit. Aperiam debitis nulla maxime deserunt illo explicabo dolor praesentium dignissimos veritatis dolore officiis cum omnis nihil, optio vitae modi officia rerum aspernatur!
                <br>
                <br>
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Cupiditate aliquam praesentium, velit quidem nostrum, facere dicta fuga nobis hic odit aut ullam excepturi culpa sunt consequuntur assumenda pariatur, debitis numquam! Lorem ipsum, dolor sit amet consectetur adipisicing elit. Corporis neque explicabo iusto! Laborum veritatis asperiores nostrum dolorem eligendi illo ducimus, architecto, sed pariatur tempora porro distinctio, incidunt illum deserunt delectus. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Debitis adipisci fugit sapiente, sit maiores soluta culpa nesciunt quam provident illo non vitae minima eligendi enim nisi dignissimos fuga, id molestiae!
                <br>
                <br>
                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Non quae molestiae ad libero, voluptate delectus illum debitis. Debitis, sunt minus eos alias quo dolores enim est eius, porro sit totam. Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis aut nam, optio unde, odio architecto tempora expedita fugit ipsa in, earum doloremque fugiat cumque praesentium nesciunt pariatur delectus obcaecati? Consequatur! Lorem ipsum, dolor sit amet consectetur adipisicing elit. Omnis tempora voluptas quidem rerum alias est, maxime quasi, ipsa eum officia nostrum sequi nisi incidunt impedit, officiis ratione. Quo, eius quibusdam? Lorem ipsum dolor sit amet consectetur, adipisicing elit. Veniam incidunt quo eveniet error ullam ab, animi blanditiis quis recusandae corrupti sequi illum quisquam praesentium iusto natus ratione provident excepturi obcaecati.
'''

employee = {
    "name":"Jon Doe",
    "title":"Head Technician",
    "years":29
}

tags = '''
<a href="#" class="tag-link">Something</a>, <a href="#" class="tag-link">Another Thing</a>, <a href="#" class="tag-link">One More Thing!</a>
'''

@app.route('/')
def main():
    return render_template('blog-template.jinja', title="Test Post, Please Ignore", employee=employee, blogbody=lorems, taglist=tags)
'''
@app.route('/<blogid>')
def getPost(blogid):
'''

@app.route('/resources/<filename>')
def statics(filename):
    return send_file("resources/{}".format(filename))

@app.route('/<filename>')
def files(filename):
    try:
        return send_file(filename)
    except:
        return "404"


