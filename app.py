
from flask import Flask, render_template,request,session
import random
app=Flask(__name__)
app.config['SECRET_KEY']='wasd'

quotes=['Goals on the road to achievement cannot be achieved without discipline and consistency. —D.Washington',
        'Your love makes me stronger, but your hate makes me unstoppable-Cristiano Ronaldo',
        'If you tell the truth, you do not have to remember anything.-Mark Twain',
        'Reality is wrong. Dreams are for real.-Tupac Shakur',
        'Surround yourself with love, not friends.-Lil Wayne',
        'Try not to become a man of success. Rather become a man of value.- Albert Einstein',
        'Victory has a thousand fathers, but defeat is an orphan. John F. Kennedy',
        ]
quote=random.choice(quotes)
print(quote)

@app.route('/')
def index():
    message='Hello Guest !'
    return render_template("index.html",quote=quote,message=message)
    

@app.route('/home')
def home():
    return 'Welcome To The Home Page'

@app.route('/bahrain')
def bahrain():
    return 'Welcome To Bahrain' 

@app.route('/unitconverter')
def unitconverter():
    return render_template("converterunit.html")

@app.route('/validateconverter')
def validateconverter():
    meter=request.args.get('meter')
    meter=float(meter)
    cm=meter*100
    return render_template("converterunit.html",result=cm)

@app.route('/vowels',methods=['GET','POST'])
def vowels():
    if request.method=='GET':
        return render_template("alphabetvc.html")    
    if request.method =='POST':
        vowels=["a","e","i","o","u"]
        letter=request.form.get('alphabet')
        print(letter)
        letter=letter.lower()
        if letter in vowels:
            return("This is a vowel")
        else:
            return("This is a consonant")

@app.route('/marks')
def marks():
    return render_template("exams.html")    

@app.route('/subject')
def subject():
    maths=request.args.get('Maths',type=float)
    science=request.args.get('Science',type=float)
    social=request.args.get('Social',type=float)
    English=request.args.get('English',type=float)
    hindi=request.args.get('Hindi',type=float)
    mean=(maths+science+social+English+hindi)/5
    return render_template("exams.html",result=mean)  

@app.route('/bmi',methods=['GET','POST'])
def bmi():
    if request.method=='GET':
        return render_template("bmi.html")    
    height=request.form.get('height',type=float)
    height=height/100
    weight=request.form.get('weight',type=float)
    bmi=weight/height**2
    message=''
    if bmi<=18.5:
        message=('This is your bmi:',bmi,'.You are underweight')
    elif 18.5>bmi <=24.9:
        message=('This is your bmi:',bmi,'. You have normal weight')
    elif 25>bmi <=29.9:
        message=('This is your bmi',bmi,'. You are over weight.')
    else:
        message=('This is your bmi',bmi,'. You are obese.')
    return render_template("bmi.html",message=message)   
    
@app.route('/bigsmall')
def bigsmall():
    return render_template("bigsmall.html")    

@app.route('/gs')
def gs():
    num1=request.args.get('num1',type=float)
    num2=request.args.get('num2',type=float)
    num3=request.args.get('num3',type=float)
    if num1>num2 and num1>num3:
        return ("The first number is greater")
    elif num2>num1 and num2>num3:
        return ("The second number is greater")
    elif num1==num2==num3:
        return("All the numbers are equal")
    else:
        return ("The third number is greater") 
        
@app.route('/courier', methods=['GET', 'POST'])
def courier():
    price=0
    if request.method=='GET': 
        return render_template("courier.html") 
    if request.method=='POST':
        weight=request.form.get("weight",type=float) 
        if weight<=20:
            if weight==20:
                price=weight*10
            elif weight>=10:
                price=weight*12
            elif weight>=1:
                price=weight*14
            elif weight<1:
                price="free of cost"
        else:
            price="we wont deliver your parcel"
        return render_template("courier.html", result=price)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='GET':
        return render_template('register.html')   
    firstname=request.form.get('firstname')
    lastname=request.form.get('lastname')
    email=request.form.get('email')
    password=request.form.get('password')
    cpassword=request.form.get('cpassword')
    message=''
    if password==cpassword:
        message='Registration successful !'
    elif password!=cpassword:
        message='Password Mismatch !'
    return render_template('register.html', message=message)



@app.route('/quotes', methods=['GET', 'POST'])
def quotes():
    pass

if __name__ == "__main__":
    app.run(debug=True)
 