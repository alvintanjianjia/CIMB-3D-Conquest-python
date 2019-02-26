from flask import Flask, request, render_template, jsonify
app = Flask(__name__)
@app.route("/", methods = ['POST', 'GET'])
def testServerRest():
    paranoidStatement = "server up and running - lol Alvin is paranoid"
    print(paranoidStatement)
    return(paranoidStatement)


@app.route("/predictSignatureImage", methods = ['POST', 'GET'])
def predictSignatureImage():
    # requestJSON = request.get_json()
    # imageBase64 = requestJSON['payload']
    # imageBase64 = imageBase64['image']
    # imageBase64 = imageBase64['imageBytes']
    #
    # print(imageBase64)
    #
    # print(requestJSON['payload'])
    #
    # create_prediction_image(imageBase64)
    #
    # file_path = 'imageToPredict.png'
    # project_id = 'cimb-demo-222703'
    # model_id = 'ICN3114570555399011330'
    #
    # with open(file_path, 'rb') as ff:
    #     content = ff.read()
    #
    #
    # prediction = get_prediction(content, project_id, model_id)
    # score = str(prediction.payload[0].classification.score)
    # answer = str(prediction.payload[0].display_name)
    return_packet = {
        'score' : 'YOUR_SCORE HERE',
        'answer': 'YOUR_ANSWER_HERE'
    }
    # response = jsonify(score, answer)
    return jsonify(return_packet)

@app.route("/predictSignatureImage", methods = ['POST', 'GET'])
def predictSignatureImage():
    # requestJSON = request.get_json()
    # imageBase64 = requestJSON['payload']
    # imageBase64 = imageBase64['image']
    # imageBase64 = imageBase64['imageBytes']
    #
    # print(imageBase64)
    #
    # print(requestJSON['payload'])
    #
    # create_prediction_image(imageBase64)
    #
    # file_path = 'imageToPredict.png'
    # project_id = 'cimb-demo-222703'
    # model_id = 'ICN3114570555399011330'
    #
    # with open(file_path, 'rb') as ff:
    #     content = ff.read()
    #
    #
    # prediction = get_prediction(content, project_id, model_id)
    # score = str(prediction.payload[0].classification.score)
    # answer = str(prediction.payload[0].display_name)
    return_packet = {
        'score' : 'YOUR_SCORE HERE',
        'answer': 'YOUR_ANSWER_HERE'
    }
    # response = jsonify(score, answer)
    return jsonify(return_packet)

# Run server
app.run(host = '192.168.0.135')