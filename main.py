import json
from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

@app.route('/post_control', methods=['POST'])
def post_control():
    try:
        data = request.get_json()
        post = data.get('post')
        communityName = data.get('communityName')
        communityDescription = data.get('communityDescription')

        print(post)
        print(communityName)
        print(communityDescription)

        key = "AIzaSyBe7_77NtUKZlMyeIQAZooTJSIQBL4eu-E"

        genai.configure(api_key=key)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')

        prompt = (
            f"Bir sosyal medya uygulamasında moderatörsün. Bu sosyal medya uygulamasının içinde bazı topluluklar "
            f"ve bu toplulukların bir oluşma amacı var. Senin görevin bu topluluklarda yapılan paylaşımları topluluğun amacına "
            f"uygunluğunu kontrol etmek. Cevabı 0 ve 1 olarak vereceksin. Eğer paylaşım topluluğun amacına uygunsa 1 uygun değilse "
            f"0 cevabını vereceksin.\n"
            f"Aşağıda verdiğim parametreler doğrultusunda"
            f"Gönderi : \"{post}\",\n"
            f"Topluluk adı : \"{communityName}\",\n"
            f"Topluluk amacı : \"{communityDescription}\",\n"
            f"Gönderideki içerik topluluk adı veya amacında bahsedilenlerle ilişkilendirilebilir mi?"
        )

        response = model.generate_content(contents=prompt)
        print(response.text)

        return jsonify({'result': response.text,}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

app.run(debug=True)