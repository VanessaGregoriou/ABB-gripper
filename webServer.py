from microdot import Microdot
from Gripper import Gripper

def startServer():
    gripper = Gripper()
    app = Microdot()
    
    @app.route('/')
    async def index(request):
        return getResponse(True, gripper.fingerDistance())

    @app.route('/gripperJog')
    async def gripperJog(request):
        print(request)
        result = gripper.jogOpen()
        return getResponse(result, gripper.fingerDistance())

    app.run(port=80, debug=True)


def getResponse(result, fingerDistance):
    html = open("index.html").read().format(fingerDistance=fingerDistance)
    return str(html), {'Content-Type': 'text/html'}

