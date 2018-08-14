from flask import Flask, request, render_template_string

"""
Lib: Flask
"""

app = Flask(__name__)


def guessing_2(check, min_num=0, max_num=1001):
    guess = int((max_num - min_num) / 2) + min_num
    if check == 3:
        return guess  # wygrana
    elif check == 1:
        max_num = guess
        guess = int((max_num - min_num) / 2) + min_num
        return [guess, min_num, max_num]
    elif check == 2:
        min_num = guess
        guess = int((max_num - min_num) / 2) + min_num
        return [guess, min_num, max_num]
    else:
        return [guess, min_num, max_num]  # start


@app.route("/", methods=['GET', 'POST'])
def form():
    # guess, min_num, max_num = guessing_2(4)
    new_form = '''
    <h4>Think about number from 0 to 1000, and I will guess it in 10 tries.</h4>
    <form method="POST">
    My guess is: {{guess_n}}</br></br>
        <input type="submit" name="more" value="More">
        <input type="submit" name="less" value="Less">
        <input type="submit" name="won" value="You won">
        <input type="hidden" name="max_num" value="{{max_n}}">
        <input type="hidden" name="min_num" value="{{min_n}}">
    </form>
    '''
    won_form = '''
            <h1>Thank you for playing. Your number was {{guess_n}}<h1>
            '''
    if request.method == 'GET':
        guess_list = guessing_2(4)
        return render_template_string(new_form, guess_n=guess_list[0], max_n=guess_list[2], min_n=guess_list[1])
    if request.method == 'POST':
        if request.values.get('more'):
            guess_list = guessing_2(2, int(request.values.get('min_num')), int(request.values.get('max_num')))
            return render_template_string(new_form, guess_n=guess_list[0], max_n=guess_list[2], min_n=guess_list[1])
        elif request.values.get('less'):
            guess_list = guessing_2(1, int(request.values.get('min_num')), int(request.values.get('max_num')))
            return render_template_string(new_form, guess_n=guess_list[0], max_n=guess_list[2], min_n=guess_list[1])
        elif request.values.get('won'):
            return render_template_string(won_form, guess_n=guessing_2(3, int(request.values.get('min_num')),
                                                                       int(request.values.get('max_num'))))


if __name__ == '__main__':
    app.run(debug=True)
