#Inicio de APP
#Adicionar o logo logotipo nos pdfs
#os campos das avaliações extraordinarias de operadores foram alterados para serem inseriodos nos campos corretos 

from flask import Flask, flash, render_template, request, redirect, url_for, session, g, Response, jsonify, make_response, send_file, send_from_directory #erro1(flash)
from datetime import date
from fpdf import FPDF
import json
import settings
from flask import Flask, render_template, request

app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "C:/Users/cafilipe/Desktop/FlaskApp/GPS/static/questionario2/"
app.secret_key = 'your secret key gpsteste'


@app.route("/download")
def download_file_questionario_op():
    path="questionario2.pdf"
    return send_file(path, as_attachment = True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/questionario',methods=['GET', 'POST'])
def questionario():
    today = date.today()

    cargo="Operador"
    teamleaders=['Diogo','Rui',Carlos]

    
    if request.method == 'POST':

        nome = request.form['nome']
        nrcol = request.form['nrcol']
        teamleader=request.form['teamleader']
        cesaa = request.form['check[]']
        cesa = ""
        oqaa=request.form['check2[]']
        oqa=""
        oraa=request.form['check4[]']
        ora=""
        riaa=request.form['check6[]']
        ria=""
        teaa=request.form['check8[]']
        tea=""
        poliaa=request.form['check10[]']
        polia=""
        ponaa=request.form['check12[]']
        pona=""
        assiaa=request.form['check14[]']
        assia=""
        apreaa=request.form['check19[]']
        aprea=""
        turno=""
        suplente=""
        contrato=""
        cestexto = request.form['cestexto']
        oqtexto = request.form['oqtexto']
        ortexto = request.form['ortexto']
        ritexto = request.form['ritexto']
        tetexto = request.form['tetexto']
        politexto = request.form['politexto']
        pontexto = request.form['pontexto']
        assitexto = request.form['assitexto']
        apretexto = request.form['apretexto']
        suptexto = ""
        
        
        if cesaa == "Abaixo":
            valor = '2.5'
        elif cesaa == "De Acordo":
            valor= '5'
        elif cesaa == "Excede":
            valor = '7.5'
        else:
            valor = '10'

        if oqaa == "Abaixo":
            valor2 = '2.5'
        elif oqaa == "De Acordo":
            valor2 = '5'
        elif oqaa == "Excede":
            valor2 = '7.5'
        else:
            valor2 = '10'
 
        if oraa == "Abaixo":
            valor4 = '2.5'
        elif oraa == "De Acordo":
            valor4 = '5'
        elif oraa == "Excede":
            valor4 = '7.5'
        else:
            valor4 = '10'

        if riaa == "Abaixo":
            valor6 = '2.5'
        elif riaa == "De Acordo":
            valor6 = '5'
        elif riaa == "Excede":
            valor6 = '7.5'
        else:
            valor6 = '10'
 
        if teaa == "Abaixo":
            valor8 = '2.5'
        elif teaa == "De Acordo":
            valor8 = '5'
        elif teaa == "Excede":
            valor8 = '7.5'
        else:
            valor8 = '10'
    
        if poliaa == "Abaixo":
            valor10 = '2.5'
        elif poliaa == "De Acordo":
            valor10 = '5'
        elif poliaa == "Excede":
            valor10 = '7.5'
        else:
            valor10 = '10'

        if ponaa == "Abaixo":
            valor12 = '0'
        else :
            valor12 = '8'

        if assiaa == "Abaixo":
            valor14 = '0'
        else:
            valor14 = '8'

        if apreaa == "Instisfatório":
            valor16='4'
        elif apreaa == "Abaixo":
            valor16 = '8'
        elif apreaa == "De Acordo":
            valor16 = '12'
        elif apreaa == "Excede":
            valor16 = '16'
        else:
            valor16 = '20'




        #avaliacaofinal= float(valor1)+float(valor3)+float(valor5)+float(valor7)+float(valor9)+float(valor11)+float(valor13)+float(valor15)+float(valor17)+float(valor18)+float(valor19)

        avaliacaofinal=""
        autoavaliacaofinal= float(valor)+float(valor2)+float(valor4)+float(valor6)+float(valor8)+float(valor10)+float(valor12)+float(valor14)+float(valor16)
        #+float(valor18)+float(valor19)

        
        maximum_value= 96

        
        conta_auto_avaliacao_final=int((autoavaliacaofinal*100)/maximum_value)
        
        print(conta_auto_avaliacao_final,'conta')

        flash('Submetido com Sucesso')
        return redirect(url_for('questionario'))



    return render_template("questionario.html",teamleaders=teamleaders)

@app.route('/questionario_extraordinario_operador',methods=['GET', 'POST'])
def questionario_extraordinario_operador():
    if 'username' not in session:
        flash('Erro!!! Sem Permissões')
        return redirect(url_for('index'))
    today = date.today()

    cargo="Operador"


    teamleaders=['Diogo','Rui','Carlos','']
    
    if request.method == 'POST':

        nome = request.form['nome']
        nrcol = request.form['nrcol']
        teamleader=request.form['teamleader']
        motivo=request.form['motivo']
        cesaa = request.form['check[]']
        cesa = ""
        oqaa=request.form['check2[]']
        oqa=""
        oraa=request.form['check4[]']
        ora=""
        riaa=request.form['check6[]']
        ria=""
        teaa=request.form['check8[]']
        tea=""
        poliaa=request.form['check10[]']
        polia=""
        ponaa=request.form['check12[]']
        pona=""
        assiaa=request.form['check14[]']
        assia=""
        apreaa=request.form['check19[]']
        aprea=""
        turno=""
        suplente=""
        contrato=""
        cestexto = request.form['cestexto']
        oqtexto = request.form['oqtexto']
        ortexto = request.form['ortexto']
        ritexto = request.form['ritexto']
        tetexto = request.form['tetexto']
        politexto = request.form['politexto']
        pontexto = request.form['pontexto']
        assitexto = request.form['assitexto']
        apretexto = request.form['apretexto']
        suptexto = ""
        
        
        if cesaa == "Abaixo":
            valor = '2.5'
        elif cesaa == "De Acordo":
            valor= '5'
        elif cesaa == "Excede":
            valor = '7.5'
        else:
            valor = '10'

        if oqaa == "Abaixo":
            valor2 = '2.5'
        elif oqaa == "De Acordo":
            valor2 = '5'
        elif oqaa == "Excede":
            valor2 = '7.5'
        else:
            valor2 = '10'
 
        if oraa == "Abaixo":
            valor4 = '2.5'
        elif oraa == "De Acordo":
            valor4 = '5'
        elif oraa == "Excede":
            valor4 = '7.5'
        else:
            valor4 = '10'

        if riaa == "Abaixo":
            valor6 = '2.5'
        elif riaa == "De Acordo":
            valor6 = '5'
        elif riaa == "Excede":
            valor6 = '7.5'
        else:
            valor6 = '10'
 
        if teaa == "Abaixo":
            valor8 = '2.5'
        elif teaa == "De Acordo":
            valor8 = '5'
        elif teaa == "Excede":
            valor8 = '7.5'
        else:
            valor8 = '10'
    
        if poliaa == "Abaixo":
            valor10 = '2.5'
        elif poliaa == "De Acordo":
            valor10 = '5'
        elif poliaa == "Excede":
            valor10 = '7.5'
        else:
            valor10 = '10'

        if ponaa == "Abaixo":
            valor12 = '0'
        else :
            valor12 = '8'

        if assiaa == "Abaixo":
            valor14 = '0'
        else:
            valor14 = '8'

        if apreaa == "Instisfatório":
            valor16='4'
        elif apreaa == "Abaixo":
            valor16 = '8'
        elif apreaa == "De Acordo":
            valor16 = '12'
        elif apreaa == "Excede":
            valor16 = '16'
        else:
            valor16 = '20'




        #avaliacaofinal= float(valor1)+float(valor3)+float(valor5)+float(valor7)+float(valor9)+float(valor11)+float(valor13)+float(valor15)+float(valor17)+float(valor18)+float(valor19)

        avaliacaofinal=""
        autoavaliacaofinal= float(valor)+float(valor2)+float(valor4)+float(valor6)+float(valor8)+float(valor10)+float(valor12)+float(valor14)+float(valor16)
        #+float(valor18)+float(valor19)

        
        maximum_value= 96

        
        conta_auto_avaliacao_final=int((autoavaliacaofinal*100)/maximum_value)
        

        flash('Submetido com Sucesso')
        return redirect(url_for('questionario_extraordinario_operador'))
    return render_template("questionario_extraordinario_operador.html",teamleaders=teamleaders)

#----------------------------
@app.route('/questionario_teamleader',methods=['GET', 'POST'])
def questionario_teamleader():
    if 'username' not in session:
        flash('Erro!!! Sem Permissões')
        return redirect(url_for('index'))
    today = date.today()

    cargo='Team Leader'

    
    pls_accounts=['Coisas']
    
    if request.method == 'POST':

        nome = session['username']
        nrcol = request.form['nrcol']
        pl=request.form['pl']
        cesaa = request.form['check[]']
        cesa = ""
        oqaa=request.form['check2[]']
        oqa=""
        oraa=request.form['check4[]']
        ora=""
        riaa=request.form['check6[]']
        ria=""
        teaa=request.form['check8[]']
        tea=""
        compeaa=request.form['check10[]']
        compea=""
        ponaa=request.form['check12[]']
        pona=""
        assiaa=request.form['check14[]']
        assia=""
        gestaoaa=request.form['check16[]']
        gestaoa=""
        apreaa=request.form['check19[]']
        aprea=""
        turno=""
        suplente=""
        contrato=""
        cestexto = request.form['cestexto']
        oqtexto = request.form['oqtexto']
        ortexto = request.form['ortexto']
        ritexto = request.form['ritexto']
        tetexto = request.form['tetexto']
        competexto = request.form['competexto']
        gestaotexto = request.form['gestaotexto']
        pontexto = request.form['pontexto']
        assitexto = request.form['assitexto']
        apretexto=request.form['apretexto']
        suptexto = ""
        
        
        if cesaa == "Abaixo":
            valor = '2.25'
        elif cesaa == "De Acordo":
            valor= '4.5'
        elif cesaa == "Excede":
            valor = '6.75'
        else:
            valor = '9'


        if oqaa == "Abaixo":
            valor2 = '2.25'
        elif oqaa == "De Acordo":
            valor2 = '4.5'
        elif oqaa == "Excede":
            valor2 = '6.75'
        else:
            valor2 = '9'
 

        if oraa == "Abaixo":
            valor4 = '2.25'
        elif oraa == "De Acordo":
            valor4 = '4.5'
        elif oraa == "Excede":
            valor4 = '6.75'
        else:
            valor4 = '9'

 
        if riaa == "Abaixo":
            valor6 = '2.25'
        elif riaa == "De Acordo":
            valor6 = '4.5'
        elif riaa == "Excede":
            valor6 = '6.75'
        else:
            valor6 = '9'


        if teaa == "Abaixo":
            valor8 = '2.25'
        elif teaa == "De Acordo":
            valor8 = '4.5'
        elif teaa == "Excede":
            valor8 = '6.75'
        else:
            valor8 = '9'
   

    
        if compeaa == "Abaixo":
            valor10 = '2.25'
        elif compeaa == "De Acordo":
            valor10 = '4.5'
        elif compeaa == "Excede":
            valor10 = '6.75'
        else:
            valor10 = '9'



        if gestaoaa == "Abaixo":
            valor18 = '2.25'
        elif gestaoaa == "De Acordo":
            valor18 = '4.5'
        elif gestaoaa == "Excede":
            valor18 = '6.75'
        else:
            valor18 = '9'


        if ponaa == "Abaixo":
            valor12 = '0'
        else :
            valor12 = '8.5'
 

        if assiaa == "Abaixo":
            valor14 = '0'
        else:
            valor14 = '8.5'

        if apreaa == "Instisfatório":
            valor16='4'
        elif apreaa == "Abaixo":
            valor16 = '8'
        elif apreaa == "De Acordo":
            valor16 = '12'
        elif apreaa == "Excede":
            valor16 = '16'
        else:
            valor16 = '20'



        #avaliacaofinal= float(valor1)+float(valor3)+float(valor5)+float(valor7)+float(valor9)+float(valor11)+float(valor13)+float(valor15)+float(valor17)+float(valor19)

        avaliacaofinal=""
        autoavaliacaofinal= float(valor)+float(valor2)+float(valor4)+float(valor6)+float(valor8)+float(valor10)+float(valor12)+float(valor14)+float(valor16)+float(valor18)

        flash('Submetido com Sucesso')
        return redirect(url_for('questionario_teamleader'))



    return render_template("questionario_teamleader.html",pls_accounts=pls_accounts)

@app.route('/questionario_tecnicomanutencao',methods=['GET', 'POST'])
def questionario_tecnicomanutencao():
    if 'username' not in session:
        flash('Erro!!! Sem Permissões')
        return redirect(url_for('index'))
    today = date.today()

    cargo='Técnico Manutenção'


    pls_accounts=['Conta','c2nta2']
    
    if request.method == 'POST':

        nome = session['username']
        nrcol = request.form['nrcol']
        pl=request.form['pl']
        cesaa = request.form['check[]']
        cesa = ""
        oqaa=request.form['check2[]']
        oqa=""
        oraa=request.form['check4[]']
        ora=""
        riaa=request.form['check6[]']
        ria=""
        teaa=request.form['check8[]']
        tea=""
        compeaa=request.form['check10[]']
        compea=""
        ponaa=request.form['check12[]']
        pona=""
        assiaa=request.form['check14[]']
        assia=""
        gestaoaa="N.A."
        gestaoa="N.A."
        apreaa=request.form['check19[]']
        aprea=""
        turno=""
        suplente=""
        contrato=""
        cestexto = request.form['cestexto']
        oqtexto = request.form['oqtexto']
        ortexto = request.form['ortexto']
        ritexto = request.form['ritexto']
        tetexto = request.form['tetexto']
        competexto = request.form['competexto']
        gestaotexto = ""
        pontexto = request.form['pontexto']
        assitexto = request.form['assitexto']
        apretexto=request.form['apretexto']
        suptexto = ""
        
        
        if cesaa == "Abaixo":
            valor = '2.25'
        elif cesaa == "De Acordo":
            valor= '4.5'
        elif cesaa == "Excede":
            valor = '6.75'
        else:
            valor = '9'


        if oqaa == "Abaixo":
            valor2 = '2.25'
        elif oqaa == "De Acordo":
            valor2 = '4.5'
        elif oqaa == "Excede":
            valor2 = '6.75'
        else:
            valor2 = '9'
 

        if oraa == "Abaixo":
            valor4 = '2.25'
        elif oraa == "De Acordo":
            valor4 = '4.5'
        elif oraa == "Excede":
            valor4 = '6.75'
        else:
            valor4 = '9'

 
        if riaa == "Abaixo":
            valor6 = '2.25'
        elif riaa == "De Acordo":
            valor6 = '4.5'
        elif riaa == "Excede":
            valor6 = '6.75'
        else:
            valor6 = '9'


        if teaa == "Abaixo":
            valor8 = '2.25'
        elif teaa == "De Acordo":
            valor8 = '4.5'
        elif teaa == "Excede":
            valor8 = '6.75'
        else:
            valor8 = '9'
   

    
        if compeaa == "Abaixo":
            valor10 = '2.25'
        elif compeaa == "De Acordo":
            valor10 = '4.5'
        elif compeaa == "Excede":
            valor10 = '6.75'
        else:
            valor10 = '9'


        if ponaa == "Abaixo":
            valor12 = '0'
        else :
            valor12 = '8.5'
 

        if assiaa == "Abaixo":
            valor14 = '0'
        else:
            valor14 = '8.5'

        if apreaa == "Instisfatório":
            valor16='4'
        elif apreaa == "Abaixo":
            valor16 = '8'
        elif apreaa == "De Acordo":
            valor16 = '12'
        elif apreaa == "Excede":
            valor16 = '16'
        else:
            valor16 = '20'



        #avaliacaofinal= float(valor1)+float(valor3)+float(valor5)+float(valor7)+float(valor9)+float(valor11)+float(valor13)+float(valor15)+float(valor17)+float(valor19)

        avaliacaofinal=""
        autoavaliacaofinal= float(valor)+float(valor2)+float(valor4)+float(valor6)+float(valor8)+float(valor10)+float(valor12)+float(valor14)+float(valor16)

        flash('Submetido com Sucesso')
        return redirect(url_for('questionario_tecnicomanutencao'))



    return render_template("questionario_tecnicomanutencao.html",pls_accounts=pls_accounts)
#----------------------------


@app.route('/questionario_avaliacao_tecnicomanutencao/<id>',methods=['GET', 'POST'])
def questionario_avaliacao_tecnicomanutencao(id):
    today = date.today()
    
    if request.method == 'POST':

        nome = request.form['nome']
        nrcol = request.form['nrcol']
        teamleader=request.form['teamleader']


        cesa = request.form['check1[]']
        oqa=request.form['check3[]']
        ora=request.form['check5[]']
        ria=request.form['check7[]']
        tea=request.form['check9[]']
        compea=request.form['check17[]']
        pona=request.form['check12[]']
        assia=request.form['check13[]']
        aprea=request.form['check20[]']

        suptexto = request.form['suptexto']
        
        """
        cestexto = request.form['cestexto']
        oqtexto = request.form['oqtexto']
        ortexto = request.form['ortexto']
        ritexto = request.form['ritexto']
        tetexto = request.form['tetexto']
        politexto = request.form['politexto']
        pontexto = request.form['pontexto']
        assitexto = request.form['assitexto']
        apretexto = request.form['apretexto']
        suptexto = request.form['suptexto']
        """
        cestexto = ""
        oqtexto = ""
        ortexto = ""
        ritexto = ""
        tetexto = ""
        pontexto = ""
        assitexto = ""
        apretexto = ""
        
        username = session['username']
        
        if cesa == "Abaixo":
            valor = '2.75'
        elif cesa == "De Acordo":
            valor= '5.5'
        elif cesa == "Excede":
            valor = '8.25'
        else:
            valor = '11'

        if oqa == "Abaixo":
            valor2 = '2.75'
        elif oqa == "De Acordo":
            valor2 = '5.5'
        elif oqa == "Excede":
            valor2 = '8.25'
        else:
            valor2 = '11'
 
        if ora == "Abaixo":
            valor4 = '2.75'
        elif ora == "De Acordo":
            valor4 = '5.5'
        elif ora == "Excede":
            valor4 = '8.25'
        else:
            valor4 = '11'

        if ria == "Abaixo":
            valor6 = '2.75'
        elif ria == "De Acordo":
            valor6 = '5.5'
        elif ria == "Excede":
            valor6 = '8.25'
        else:
            valor6 = '11'
 
        if tea == "Abaixo":
            valor8 = '2.75'
        elif tea == "De Acordo":
            valor8 = '5.5'
        elif tea == "Excede":
            valor8 = '8.25'
        else:
            valor8 = '11'
    
        if compea == "Abaixo":
            valor10 = '2.75'
        elif compea == "De Acordo":
            valor10 = '5.5'
        elif compea == "Excede":
            valor10 = '8.25'
        else:
            valor10 = '11'

        if pona == "Abaixo":
            valor12 = '0'
        else :
            valor12 = '7'

        if assia == "Abaixo":
            valor14 = '0'
        else:
            valor14 = '7'

        if aprea == "Instisfatório":
            valor16='4'
        elif aprea == "Abaixo":
            valor16 = '8'
        elif aprea == "De Acordo":
            valor16 = '12'
        elif aprea == "Excede":
            valor16 = '16'
        else:
            valor16 = '20'


        #avaliacaofinal= float(valor1)+float(valor3)+float(valor5)+float(valor7)+float(valor9)+float(valor11)+float(valor13)+float(valor15)+float(valor17)+float(valor18)+float(valor19)
        avaliacaofinal= float(valor)+float(valor2)+float(valor4)+float(valor6)+float(valor8)+float(valor10)+float(valor12)+float(valor14)+float(valor16)


  

        flash('Submetido com Sucesso')
        return redirect(url_for('minhas_avaliacoes_pl'))



    return render_template("minhas_avaliacoes_pl.html",teamleaders=teamleaders)
#----------------------------



#----------------------------
@app.route('/propria_avaliacao', methods=['POST','GET'])
def propria_avaliacao():
    today = date.today()
    nome=session['username']
    
    minha_avaliacao=['Coisas']
    pls_accounts=['Coisas23']
    
    return render_template('propria_avaliacao.html',minha_avaliacao=minha_avaliacao,pls_accounts=pls_accounts,today=today)

@app.route('/propria_avaliacao_tecnico', methods=['POST','GET'])
def propria_avaliacao_tecnico():
    today = date.today()
    nome=session['username']
    return render_template('propria_avaliacao_tecnico.html',today=today)
#------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        #con=conn2.cursor()
        #con.execute('SELECT * FROM account WHERE username = ? AND password = ?', (username, password))
        # Fetch one record and return result em array
        #account = con.fetchone()
        # If account exists in accounts table in out database
        #if account:
            # Create session data, we can access this data in other routes mas temos de selecioanr a linha de array
            #session['loggedin'] = True
            
        session['username'] = username
        session['password'] = password
        session['worknumber'] = '000222'
        session['acesslevel'] = 1
        # Redirect to home page
        if session['acesslevel'] == 2 :
            return redirect(url_for('minhas_avaliacoes'))
        elif session['acesslevel'] == 3: 
            return redirect(url_for('minhas_avaliacoes_pl'))
        elif session['acesslevel'] == 1:
            return redirect(url_for('minhas_avaliacoes'))
        else: 
            return redirect(url_for('home')) 
    else:
        flash('Wrong Username / Password')
        return redirect(url_for('index'))



#------------------------------------------
@app.route('/home',methods=['GET', 'POST'])
def home():     
        username=session['username']
        ole="users"
        users='oles'
        
        return render_template('home.html',ole=ole,users=users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index')) 
    #return render_template("index.html")
#------------------------------------------
@app.route('/opquest',methods=['GET', 'POST'])
def opquest():
  
    today = date.today()
    cargo="Operador"
    teamleaders=["isto1","isto2"]
    
    if request.method == 'POST':

        nome = request.form['nome']
        nrcol = request.form['nrcol']
        cesaa = request.form['check[]']
        cesa = request.form['check1[]']
        oqaa=request.form['check2[]']
        oqa=request.form['check3[]']
        oraa=request.form['check4[]']
        ora=request.form['check5[]']
        riaa=request.form['check6[]']
        ria=request.form['check7[]']
        teaa=request.form['check8[]']
        tea=request.form['check9[]']
        poliaa=request.form['check10[]']
        polia=request.form['check11[]']
        ponaa=request.form['check12[]']
        pona=request.form['check13[]']
        assiaa=request.form['check14[]']
        assia=request.form['check15[]']
        apreaa=request.form['check19[]']
        aprea=request.form['check20[]']
        turno=request.form['check16[]']
        suplente=request.form['check17[]']
        contrato=request.form['check18[]']
        cestexto = request.form['cestexto']
        oqtexto = request.form['oqtexto']
        ortexto = request.form['ortexto']
        ritexto = request.form['ritexto']
        tetexto = request.form['tetexto']
        politexto = request.form['politexto']
        pontexto = request.form['pontexto']
        assitexto = request.form['assitexto']
        apretexto = request.form['apretexto']
        suptexto = request.form['suptexto']
        username = session['username']
        teamleader=request.form['teamleader']



        if cesaa == "Abaixo":
            valor = '2.5'
        elif cesaa == "De Acordo":
            valor= '5'
        elif cesaa == "Excede":
            valor = '7.5'
        else:
            valor = '10'

        if cesa == "Abaixo":
            valor1 = '2.5'
        elif cesa == "De Acordo":
            valor1 = '5'
        elif cesa == "Excede":
            valor1 = '7.5'
        else:
            valor1 = '10'

        if oqaa == "Abaixo":
            valor2 = '2.5'
        elif oqaa == "De Acordo":
            valor2 = '5'
        elif oqaa == "Excede":
            valor2 = '7.5'
        else:
            valor2 = '10'
 
        if oqa == "Abaixo":
            valor3 = '2.5'
        elif oqa == "De Acordo":
            valor3 = '5'
        elif oqa == "Excede":
            valor3 = '7.5'
        else:
            valor3 = '10'

        if oraa == "Abaixo":
            valor4 = '2.5'
        elif oraa == "De Acordo":
            valor4 = '5'
        elif oraa == "Excede":
            valor4 = '7.5'
        else:
            valor4 = '10'

        if ora == "Abaixo":
            valor5 = '2.5'
        elif ora == "De Acordo":
            valor5 = '5'
        elif ora == "Excede":
            valor5 = '7.5'
        else:
            valor5 = '10'
 
        if riaa == "Abaixo":
            valor6 = '2.5'
        elif riaa == "De Acordo":
            valor6 = '5'
        elif riaa == "Excede":
            valor6 = '7.5'
        else:
            valor6 = '10'
 
        if ria == "Abaixo":
            valor7 = '2.5'
        elif ria == "De Acordo":
            valor7 = '5'
        elif ria == "Excede":
            valor7 = '7.5'
        else:
            valor7 = '10'

        if teaa == "Abaixo":
            valor8 = '2.5'
        elif teaa == "De Acordo":
            valor8 = '5'
        elif teaa == "Excede":
            valor8 = '7.5'
        else:
            valor8 = '10'
   

        if tea == "Abaixo":
            valor9 = '2.5'
        elif tea == "De Acordo":
            valor9 = '5'
        elif tea == "Excede":
            valor9 = '7.5'
        else:
            valor9 = '10'
    
        if poliaa == "Abaixo":
            valor10 = '2.5'
        elif poliaa == "De Acordo":
            valor10 = '5'
        elif poliaa == "Excede":
            valor10 = '7.5'
        else:
            valor10 = '10'

        if polia == "Abaixo":
            valor11 = '2.5'
        elif polia == "De Acordo":
            valor11 = '5'
        elif polia == "Excede":
            valor11 = '7.5'
        else:
            valor11 = '10'

        if ponaa == "Abaixo":
            valor12 = '0'
        else :
            valor12 = '8'
 
        if pona == "Abaixo":
            valor13 = '0'
        else:
            valor13 = '8'

        if assiaa == "Abaixo":
            valor14 = '0'
        else:
            valor14 = '8'

        if assia == "Abaixo":
            valor15 = '0'
        else :
            valor15 = '8'

        if apreaa == "Instisfatório":
            valor16='4'
        elif apreaa == "Abaixo":
            valor16 = '8'
        elif apreaa == "De Acordo":
            valor16 = '12'
        elif apreaa == "Excede":
            valor16 = '16'
        else:
            valor16 = '20'

        if aprea == "Instisfatório":
            valor17='4'
        elif aprea == "Abaixo":
            valor17 = '8'
        elif aprea == "De Acordo":
            valor17 = '12'
        elif aprea == "Excede":
            valor17 = '16'
        else:
            valor17 = '20'

        if turno == "Sim":
            valor18 = '2'
        else:
            valor18 = '0'

        if suplente == "Sim":
            valor19 = '2'
        else:
            valor19 = '0'


        avaliacaofinal= float(valor1)+float(valor3)+float(valor5)+float(valor7)+float(valor9)+float(valor11)+float(valor13)+float(valor15)+float(valor17)+float(valor18)+float(valor19)


        autoavaliacaofinal= float(valor)+float(valor2)+float(valor4)+float(valor6)+float(valor8)+float(valor10)+float(valor12)+float(valor14)+float(valor16)+float(valor18)+float(valor19)

        maximum_value= 96

        
        conta_auto_avaliacao_final=int((autoavaliacaofinal*100)/maximum_value)
        

        return redirect(url_for('home'))



    return render_template("opquest.html",teamleaders=teamleaders)

@app.route('/tlquest',methods=['GET', 'POST'])
def tlquest():

    today = date.today()
    cargo="Chefe de Equipa"
   

    if request.method == 'POST':

        nome = request.form['nome']
        nrcol = request.form['nrcol']
        cesaa = request.form['check[]']
        cesa = request.form['check1[]']
        oqaa=request.form['check2[]']
        oqa=request.form['check3[]']
        oraa=request.form['check4[]']
        ora=request.form['check5[]']
        riaa=request.form['check6[]']
        ria=request.form['check7[]']
        teaa=request.form['check8[]']
        tea=request.form['check9[]']
        compeaa=request.form['check10[]']
        compea=request.form['check11[]']
        gestaoaa=request.form['check16[]']
        gestaoa=request.form['check17[]']
        ponaa=request.form['check12[]']
        pona=request.form['check13[]']
        assiaa=request.form['check14[]']
        assia=request.form['check15[]']
        apreaa=request.form['check19[]']
        aprea=request.form['check20[]']
        cestexto = request.form['cestexto']
        oqtexto = request.form['oqtexto']
        ortexto = request.form['ortexto']
        ritexto = request.form['ritexto']
        tetexto = request.form['tetexto']
        competexto = request.form['competexto']
        gestaotexto = request.form['gestaotexto']
        pontexto = request.form['pontexto']
        assitexto = request.form['assitexto']
        apretexto = request.form['apretexto']
        suptexto = request.form['suptexto']
        username = session['username']



        if cesaa == "Abaixo":
            valor = '2.25'
        elif cesaa == "De Acordo":
            valor= '4.5'
        elif cesaa == "Excede":
            valor = '6.75'
        else:
            valor = '9'

        if cesa == "Abaixo":
            valor1 = '2.25'
        elif cesa == "De Acordo":
            valor1 = '4.5'
        elif cesa == "Excede":
            valor1 = '6.75'
        else:
            valor1 = '9'

        if oqaa == "Abaixo":
            valor2 = '2.25'
        elif oqaa == "De Acordo":
            valor2 = '4.5'
        elif oqaa == "Excede":
            valor2 = '6.75'
        else:
            valor2 = '9'
 
        if oqa == "Abaixo":
            valor3 = '2.25'
        elif oqa == "De Acordo":
            valor3 = '4.5'
        elif oqa == "Excede":
            valor3 = '6.75'
        else:
            valor3 = '9'

        if oraa == "Abaixo":
            valor4 = '2.25'
        elif oraa == "De Acordo":
            valor4 = '4.5'
        elif oraa == "Excede":
            valor4 = '6.75'
        else:
            valor4 = '9'

        if ora == "Abaixo":
            valor5 = '2.25'
        elif ora == "De Acordo":
            valor5 = '4.5'
        elif ora == "Excede":
            valor5 = '6.75'
        else:
            valor5 = '9'
 
        if riaa == "Abaixo":
            valor6 = '2.25'
        elif riaa == "De Acordo":
            valor6 = '4.5'
        elif riaa == "Excede":
            valor6 = '6.75'
        else:
            valor6 = '9'
 
        if ria == "Abaixo":
            valor7 = '2.25'
        elif ria == "De Acordo":
            valor7 = '4.5'
        elif ria == "Excede":
            valor7 = '6.75'
        else:
            valor7 = '9'

        if teaa == "Abaixo":
            valor8 = '2.25'
        elif teaa == "De Acordo":
            valor8 = '4.5'
        elif teaa == "Excede":
            valor8 = '6.75'
        else:
            valor8 = '9'
   

        if tea == "Abaixo":
            valor9 = '2.25'
        elif tea == "De Acordo":
            valor9 = '4.5'
        elif tea == "Excede":
            valor9 = '6.75'
        else:
            valor9 = '9'
    
        if compeaa == "Abaixo":
            valor10 = '2.25'
        elif compeaa == "De Acordo":
            valor10 = '4.5'
        elif compeaa == "Excede":
            valor10 = '6.75'
        else:
            valor10 = '9'

        if compea == "Abaixo":
            valor11 = '2.25'
        elif compea == "De Acordo":
            valor11 = '4.5'
        elif compea == "Excede":
            valor11 = '6.75'
        else:
            valor11 = '9'

        if gestaoaa == "Abaixo":
            valor18 = '2.25'
        elif gestaoaa == "De Acordo":
            valor18 = '4.5'
        elif gestaoaa == "Excede":
            valor18 = '6.75'
        else:
            valor18 = '9'

        if gestaoa == "Abaixo":
            valor19 = '2.25'
        elif gestaoa == "De Acordo":
            valor19 = '4.5'
        elif gestaoa == "Excede":
            valor19 = '6.75'
        else:
            valor19 = '9'

        if ponaa == "Abaixo":
            valor12 = '0'
        else :
            valor12 = '8.5'
 
        if pona == "Abaixo":
            valor13 = '0'
        else:
            valor13 = '8.5'

        if assiaa == "Abaixo":
            valor14 = '0'
        else:
            valor14 = '8.5'

        if assia == "Abaixo":
            valor15 = '0'
        else :
            valor15 = '8.5'

        if apreaa == "Instisfatório":
            valor16='4'
        elif apreaa == "Abaixo":
            valor16 = '8'
        elif apreaa == "De Acordo":
            valor16 = '12'
        elif apreaa == "Excede":
            valor16 = '16'
        else:
            valor16 = '20'

        if aprea == "Instisfatório":
            valor17='4'
        elif aprea == "Abaixo":
            valor17 = '8'
        elif aprea == "De Acordo":
            valor17 = '12'
        elif aprea == "Excede":
            valor17 = '16'
        else:
            valor17 = '20'



        avaliacaofinal= float(valor1)+float(valor3)+float(valor5)+float(valor7)+float(valor9)+float(valor11)+float(valor13)+float(valor15)+float(valor17)+float(valor19)


        autoavaliacaofinal= float(valor)+float(valor2)+float(valor4)+float(valor6)+float(valor8)+float(valor10)+float(valor12)+float(valor14)+float(valor16)+float(valor18)

        return redirect(url_for('home'))





    return render_template('tlquest.html')

@app.route('/tmquest',methods=['GET', 'POST'])
def tmquest():

    conn2=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.30.64.42;DATABASE=GPS;UID=gps_user;PWD=gps_user123!')

    cargo="Técnico"
    today = date.today()

    if request.method == 'POST':
        #Ir buscar ao formulário os campos preenchidos
        nome = request.form['nome']
        nrcol = request.form['nrcol']
        cesaa = request.form['check[]']
        cesa = request.form['check1[]']
        oqaa=request.form['check2[]']
        oqa=request.form['check3[]']
        oraa=request.form['check4[]']
        ora=request.form['check5[]']
        riaa=request.form['check6[]']
        ria=request.form['check7[]']
        teaa=request.form['check8[]']
        tea=request.form['check9[]']
        compeaa=request.form['check10[]']
        compea=request.form['check11[]']
        ponaa=request.form['check12[]']
        pona=request.form['check13[]']
        assiaa=request.form['check14[]']
        assia=request.form['check15[]']
        apreaa=request.form['check19[]']
        aprea=request.form['check20[]']
        cestexto = request.form['cestexto']
        oqtexto = request.form['oqtexto']
        ortexto = request.form['ortexto']
        ritexto = request.form['ritexto']
        tetexto = request.form['tetexto']
        competexto = request.form['competexto']
        pontexto = request.form['pontexto']
        assitexto = request.form['assitexto']
        apretexto = request.form['apretexto']
        suptexto = request.form['suptexto']
        username = session['username']

        #Calculo da avaliação e auto avaliação
        if cesaa == "Abaixo":
            valor = '2.75'
        elif cesaa == "De Acordo":
            valor= '5.5'
        elif cesaa == "Excede":
            valor = '8.25'
        else:
            valor = '11'

        if cesa == "Abaixo":
            valor1 = '2.75'
        elif cesa == "De Acordo":
            valor1 = '5.5'
        elif cesa == "Excede":
            valor1 = '8.25'
        else:
            valor1 = '11'

        if oqaa == "Abaixo":
            valor2 = '2.75'
        elif oqaa == "De Acordo":
            valor2 = '5.5'
        elif oqaa == "Excede":
            valor2 = '8.25'
        else:
            valor2 = '11'
 
        if oqa == "Abaixo":
            valor3 = '2.75'
        elif oqa == "De Acordo":
            valor3 = '5.5'
        elif oqa == "Excede":
            valor3 = '8.25'
        else:
            valor3 = '11'

        if oraa == "Abaixo":
            valor4 = '2.75'
        elif oraa == "De Acordo":
            valor4 = '5.5'
        elif oraa == "Excede":
            valor4 = '8.25'
        else:
            valor4 = '11'

        if ora == "Abaixo":
            valor5 = '2.75'
        elif ora == "De Acordo":
            valor5 = '5.5'
        elif ora == "Excede":
            valor5 = '8.25'
        else:
            valor5 = '11'
 
        if riaa == "Abaixo":
            valor6 = '2.75'
        elif riaa == "De Acordo":
            valor6 = '5.5'
        elif riaa == "Excede":
            valor6 = '8.25'
        else:
            valor6 = '11'
 
        if ria == "Abaixo":
            valor7 = '2.75'
        elif ria == "De Acordo":
            valor7 = '5.5'
        elif ria == "Excede":
            valor7 = '8.25'
        else:
            valor7 = '11'

        if teaa == "Abaixo":
            valor8 = '2.75'
        elif teaa == "De Acordo":
            valor8 = '5.5'
        elif teaa == "Excede":
            valor8 = '8.25'
        else:
            valor8 = '11'
   

        if tea == "Abaixo":
            valor9 = '2.75'
        elif tea == "De Acordo":
            valor9 = '5.5'
        elif tea == "Excede":
            valor9 = '8.25'
        else:
            valor9 = '11'
    
        if compeaa == "Abaixo":
            valor10 = '2.75'
        elif compeaa == "De Acordo":
            valor10 = '5.5'
        elif compeaa == "Excede":
            valor10 = '8.25'
        else:
            valor10 = '11'

        if compea == "Abaixo":
            valor11 = '2.75'
        elif compea == "De Acordo":
            valor11 = '5.5'
        elif compea == "Excede":
            valor11 = '8.25'
        else:
            valor11 = '11'

        if ponaa == "Abaixo":
            valor12 = '0'
        else :
            valor12 = '7'
 
        if pona == "Abaixo":
            valor13 = '0'
        else:
            valor13 = '7'

        if assiaa == "Abaixo":
            valor14 = '0'
        else:
            valor14 = '7'

        if assia == "Abaixo":
            valor15 = '0'
        else :
            valor15 = '7'

        if apreaa == "Instisfatório":
            valor16='4'
        elif apreaa == "Abaixo":
            valor16 = '8'
        elif apreaa == "De Acordo":
            valor16 = '12'
        elif apreaa == "Excede":
            valor16 = '16'
        else:
            valor16 = '20'

        if aprea == "Instisfatório":
            valor17='4'
        elif aprea == "Abaixo":
            valor17 = '8'
        elif aprea == "De Acordo":
            valor17 = '12'
        elif aprea == "Excede":
            valor17 = '16'
        else:
            valor17 = '20'



        avaliacaofinal= float(valor1)+float(valor3)+float(valor5)+float(valor7)+float(valor9)+float(valor11)+float(valor13)+float(valor15)+float(valor17)


        autoavaliacaofinal= float(valor)+float(valor2)+float(valor4)+float(valor6)+float(valor8)+float(valor10)+float(valor12)+float(valor14)+float(valor16)


        return redirect(url_for('home'))




    return render_template('tmquest.html')
#------------------------------------------


@app.route('/teamleader_list_pl',methods=['GET', 'POST'])
def teamleader_list_pl():
    try: 
        username=session['username']
        cargo="Team Leader"

        teamleader_list=["teste2"]
       
        
        return render_template('teamleader_list_pl.html', teamleader_list=teamleader_list)
    except:
        flash('Tem que fazer login!')
        return redirect(url_for('index'))



#------------------------------------------
@app.route('/minhas_avaliacoes',methods=['GET', 'POST'])
def minhas_avaliacoes():
    today = date.today()
    try: 
        username=session['username']
        #Conexão com a base de dados, e listagem dos operadores
            
        
        return render_template('minhas_avaliacoes.html',today=today)
    except:
        flash('Tem que fazer login!')
        return redirect(url_for('index'))

    return render_template('minhas_avaliacoes.html')

#------------------------------
@app.route('/table_operador/<int:id>')
def table_operador(id):

    con=conn2.cursor()
    con.execute('SELECT * FROM opquest WHERE id = {0}' .format(id))  
    minha_avaliacao=con.fetchall()
    con.close()
    today = date.today()

    for row in minha_avaliacao:
        # Make a PDF straight from HTML in a string.
        pdf = FPDF()

        pdf.add_page()
        
        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font('Times','B',16) 
        pdf.cell(page_width, 0.0, 'Avaliação - '+ str(row[35]), align='R')
        pdf.image("static/content/BorgWarner_Technology_Blue.png", 10,10,80,10)
        pdf.set_font('Times', '', 14)
        
        col_width = page_width/2
        col_width_small = page_width/4
             
        th = pdf.font_size

        pdf.ln(15)

        pdf.cell(60, th, 'Data: '+ str(row[2]), border=0)
        pdf.cell(60, th, 'Colaborador/a: '+ str(row[35]), border=0)
        pdf.cell(60, th, 'Team Leader: '+ str(row[1]), border=0)
        pdf.ln(15)
  
        pdf.cell(col_width, th, '', border=0)
        pdf.cell(col_width_small, th, 'Autoavaliação', border=1)
        pdf.cell(col_width_small, th, 'Avaliação', border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Cultura e Segurança', border=1)
        pdf.cell(col_width_small, th, row[3], border=1)
        pdf.cell(col_width_small, th, row[4], border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Orientação Qualidade', border=1)
        pdf.cell(col_width_small, th, row[5], border=1)
        pdf.cell(col_width_small, th, row[6], border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Orientação Resultados', border=1)
        pdf.cell(col_width_small, th, row[7], border=1)
        pdf.cell(col_width_small, th, row[8], border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Relacionamento Interpessoal', border=1)
        pdf.cell(col_width_small, th, row[9], border=1)
        pdf.cell(col_width_small, th, row[10], border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Trabalho Equipa', border=1)
        pdf.cell(col_width_small, th, row[11], border=1)
        pdf.cell(col_width_small, th, row[12], border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Polivalência', border=1)
        pdf.cell(col_width_small, th, row[13], border=1)
        pdf.cell(col_width_small, th, row[14], border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Pontualidade', border=1)
        pdf.cell(col_width_small, th, row[15], border=1)
        pdf.cell(col_width_small, th, row[16], border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Assiduidade', border=1)
        pdf.cell(col_width_small, th, row[17], border=1)
        pdf.cell(col_width_small, th, row[18], border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Apreciação Global', border=1)
        pdf.cell(col_width_small, th, row[19], border=1)
        pdf.cell(col_width_small, th, row[20], border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Outros Turnos', border=1)
        pdf.cell(col_width_small, th,'' , border=1)
        pdf.cell(col_width_small, th, row[21], border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Trabalho Suplementar', border=1)
        pdf.cell(col_width_small, th, row[4], border=1)
        pdf.cell(col_width_small, th, row[5], border=1)
        pdf.ln(th)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Final', border=1)
        pdf.cell(col_width_small, th, str(row[37]), border=1)
        pdf.cell(col_width_small, th, str(row[24]), border=1)
        pdf.ln(th)
 
        pdf.set_font('Times','',14.0)
        texto_notas='Notas: '+str(row[34])
        #pdf.cell(page_width, th,'Notas: ' +str(row[34]))
        pdf.multi_cell(0, 5, texto_notas)
        pdf.ln(th)
        pdf.ln(th)
        
        text_compromisso_honra='Eu, ' + str(row[1]) + ' Team Leader de ' +  str(row[35]) + ' confirmo, sob compromisso de honra, que a pessoa mencionada tomou conhecimento da presente avaliação.'   
        pdf.multi_cell(0, 5, text_compromisso_honra)
        pdf.ln(th)  
        return Response(bytes(pdf.output(dest='S')), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=avaliacao_'+str(row[35])+'.pdf'}) 


@app.route('/table_operador_extra/<int:id>')
def table_operador_extra(id):

    con=conn2.cursor()
    con.execute('SELECT * FROM opquest WHERE id = {0}' .format(id))  
    minha_avaliacao=con.fetchall()
    con.close()
    today = date.today()

    

    for row in minha_avaliacao:
        # Make a PDF straight from HTML in a string.

        pdf = FPDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True,margin = 20)
       
        
        page_width = pdf.w - 2 * pdf.l_margin
        print (page_width)
        pdf.set_font('Times','B',16) 
        pdf.cell(190, 0.0, 'Avaliação: '+ str(row[35]), align='R')
        pdf.ln(6)
        pdf.cell(190, 0.0, 'Motivo: '+ str(row[45]), align='R')
        pdf.image("static/content/BorgWarner_Technology_Blue.png", 10,10,80,10)
        pdf.set_font('Times', '', 14)
        
        col_width = page_width/2
        col_width_small = page_width/4
             
        pdf.ln(1)
             
        th = pdf.font_size
     
        pdf.ln(15)

        pdf.cell(60, th, 'Data: '+ str(row[2]), border=0)
        pdf.cell(60, th, 'Colaborador/a: '+ str(row[35]), border=0)
        pdf.cell(60, th, 'Team Leader: '+ str(row[1]), border=0)
        pdf.ln(15)
        pdf.set_font('Times','B',16) 
        pdf.cell(col_width_small, th, 'Cultura e Segurança', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 12)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[3]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[25]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',16) 
        pdf.cell(col_width_small, th, 'Orientação Qualidade', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 12)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[4]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[26]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',16) 
        pdf.cell(col_width_small, th, 'Orientação Resultados', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 12)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[7]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[27]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',16) 
        pdf.cell(col_width_small, th, 'Relacionamento Interpessoal', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 12)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[9]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[28]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',16) 
        pdf.cell(col_width_small, th, 'Trabalho Equipa', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 12)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[11]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[29]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',16) 
        pdf.cell(col_width_small, th, 'Polivalência', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 12)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[13]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[30]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',16) 
        pdf.cell(col_width_small, th, 'Pontualidade', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 12)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[15]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[31]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',16) 
        pdf.cell(col_width_small, th, 'Assiduidade', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 12)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[17]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[32]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',16) 
        pdf.cell(col_width_small, th, 'Apreciação Global', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 12)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[19]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[33]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',16) 
        pdf.cell(col_width_small, th, 'Avaliação final', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 12)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[37]), border=0)

        pdf.ln(8)
    
        pdf.set_font('Times','',12)
        text_compromisso_honra='Eu, ' + str(row[1]) + ' Team Leader do colaborador/a,  ' +  str(row[35]) + ' realizei esta avaliação extraordinária pelo motivo - "'+ str(row[45])+'" .'   
        pdf.multi_cell(0, 5, text_compromisso_honra)

        return Response(bytes(pdf.output(dest='S')), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=avaliacao_'+str(row[35])+'.pdf'}) 

@app.route('/table_tecnico_pl/<int:id>')
def table_tecnico_pl(id):

    con=conn2.cursor()
    con.execute('SELECT * FROM tlquest WHERE id = {0}' .format(id))  
    minha_avaliacao=con.fetchall()
    con.close()
    today = date.today()

    for row in minha_avaliacao:
        # Make a PDF straight from HTML in a string.
        pdf = FPDF()

        pdf.add_page()
        pdf.set_font('Times', 'B', 15)
        pdf.image("static/content/BorgWarner_Technology_Blue.png", 25,20,160,20)


        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Avaliação - '+ str(row[4]), align='C')
        pdf.ln(30)
        pdf.set_font('Times', '', 14)
        
        col_width = page_width/2
        col_width_small = page_width/4
             
        pdf.ln(1)
             
        th = pdf.font_size
        
        pdf.cell(col_width_small, th, 'Data: '+ str(row[3]), border=0)
        pdf.ln(th)
        pdf.ln(th)
        pdf.cell(col_width_small, th, 'Técnico '+ str(row[4]), border=0)
        pdf.ln(th)
        pdf.ln(th)
        pdf.cell(col_width_small, th, 'Product Leader: '+ str(row[1]), border=0)
        pdf.ln(th)
        pdf.ln(th)
        pdf.ln(th)
        pdf.cell(col_width, th, '', border=0)
        pdf.cell(col_width_small, th, 'Autoavaliação', border=1)
        pdf.cell(col_width_small, th, 'Avaliação', border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Cultura e Segurança', border=1)
        pdf.cell(col_width_small, th, str(row[6]), border=1)
        pdf.cell(col_width_small, th, str(row[7]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Orientação Qualidade', border=1)
        pdf.cell(col_width_small, th, str(row[8]), border=1)
        pdf.cell(col_width_small, th, str(row[9]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Orientação Resultados', border=1)
        pdf.cell(col_width_small, th, str(row[10]), border=1)
        pdf.cell(col_width_small, th, str(row[11]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Relacionamento Interpessoal', border=1)
        pdf.cell(col_width_small, th, str(row[12]), border=1)
        pdf.cell(col_width_small, th, str(row[13]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Trabalho Equipa', border=1)
        pdf.cell(col_width_small, th, str(row[14]), border=1)
        pdf.cell(col_width_small, th, str(row[15]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Competencias Tec.', border=1)
        pdf.cell(col_width_small, th, str(row[16]), border=1)
        pdf.cell(col_width_small, th, str(row[17]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Pontualidade', border=1)
        pdf.cell(col_width_small, th, str(row[20]), border=1)
        pdf.cell(col_width_small, th, str(row[21]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Assiduidade', border=1)
        pdf.cell(col_width_small, th, str(row[22]), border=1)
        pdf.cell(col_width_small, th, str(row[23]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Apreciação Global', border=1)
        pdf.cell(col_width_small, th, str(row[24]), border=1)
        pdf.cell(col_width_small, th, str(row[25]), border=1)
        pdf.ln(th)
        pdf.ln(th)
        pdf.set_font('Times','',14.0)
        pdf.cell(col_width, th, 'Final', border=1)
        pdf.cell(col_width_small, th, str(row[38]), border=1)
        pdf.cell(col_width_small, th, str(row[37]), border=1)
        pdf.ln(th)
        pdf.ln(th)   
        pdf.set_font('Times','',14.0)
        texto_notas='Notas: '+str(row[36])

        pdf.multi_cell(0, 5, texto_notas)
        pdf.ln(th)
        pdf.ln(th)
        
        text_compromisso_honra='Eu, ' + str(row[1]) + ' Product Leader de ' +  str(row[4]) + ' confirmo, sob compromisso de honra, que a pessoa mencionada tomou conhecimento da presente avaliação.'   
        pdf.multi_cell(0, 5, text_compromisso_honra)
        pdf.ln(th)  
        pdf.ln(th)  

        pdf.cell(page_width, th,'Data: '+ str(row[39]), align='C')

        return Response(pdf.output(dest='S').encode('latin-1'), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=Avaliação '+str(row[4])+'.pdf'})


@app.route('/table_team_leader_pl/<int:id>')
def table_team_leader_pl(id):

    con=conn2.cursor()
    con.execute('SELECT * FROM tlquest WHERE id = {0}' .format(id))  
    minha_avaliacao=con.fetchall()
    con.close()
    today = date.today()

    for row in minha_avaliacao:
        # Make a PDF straight from HTML in a string.
        pdf = FPDF()

        pdf.add_page()
        pdf.set_font('Times', 'B', 15)
        pdf.image("static/content/BorgWarner_Technology_Blue.png", 25,20,160,20)


        page_width = pdf.w - 2 * pdf.l_margin

        pdf.set_font('Times','B',14.0) 
        pdf.cell(page_width, 0.0, 'Avaliação - '+ str(row[4]), align='C')
        pdf.ln(30)
        pdf.set_font('Times', '', 14)
        
        col_width = page_width/2
        col_width_small = page_width/4
             
        pdf.ln(1)
             
        th = pdf.font_size
        
        pdf.cell(col_width_small, th, 'Data: '+ str(row[3]), border=0)
        pdf.ln(th)
        pdf.ln(th)
        pdf.cell(col_width_small, th, 'Team Leader '+ str(row[4]), border=0)
        pdf.ln(th)
        pdf.ln(th)
        pdf.cell(col_width_small, th, 'Product Leader: '+ str(row[1]), border=0)
        pdf.ln(th)
        pdf.ln(th)
        pdf.ln(th)
        pdf.cell(col_width, th, '', border=0)
        pdf.cell(col_width_small, th, 'Autoavaliação', border=1)
        pdf.cell(col_width_small, th, 'Avaliação', border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Cultura e Segurança', border=1)
        pdf.cell(col_width_small, th, str(row[6]), border=1)
        pdf.cell(col_width_small, th, str(row[7]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Orientação Qualidade', border=1)
        pdf.cell(col_width_small, th, str(row[8]), border=1)
        pdf.cell(col_width_small, th, str(row[9]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Orientação Resultados', border=1)
        pdf.cell(col_width_small, th, str(row[10]), border=1)
        pdf.cell(col_width_small, th, str(row[11]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Relacionamento Interpessoal', border=1)
        pdf.cell(col_width_small, th, str(row[12]), border=1)
        pdf.cell(col_width_small, th, str(row[13]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Trabalho Equipa', border=1)
        pdf.cell(col_width_small, th, str(row[14]), border=1)
        pdf.cell(col_width_small, th, str(row[15]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Competencias Tec.', border=1)
        pdf.cell(col_width_small, th, str(row[16]), border=1)
        pdf.cell(col_width_small, th, str(row[17]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Pontualidade', border=1)
        pdf.cell(col_width_small, th, str(row[20]), border=1)
        pdf.cell(col_width_small, th, str(row[21]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Assiduidade', border=1)
        pdf.cell(col_width_small, th, str(row[22]), border=1)
        pdf.cell(col_width_small, th, str(row[23]), border=1)
        pdf.ln(th)
        pdf.cell(col_width, th, 'Apreciação Global', border=1)
        pdf.cell(col_width_small, th, str(row[24]), border=1)
        pdf.cell(col_width_small, th, str(row[25]), border=1)
        pdf.ln(th)
        pdf.ln(th)
        pdf.set_font('Times','',14.0)
        pdf.cell(col_width, th, 'Final', border=1)
        pdf.cell(col_width_small, th, str(row[38]), border=1)
        pdf.cell(col_width_small, th, str(row[37]), border=1)
        pdf.ln(th)
        pdf.ln(th)   
        pdf.set_font('Times','',14.0)
        texto_notas='Notas: '+str(row[36])

        pdf.multi_cell(0, 5, texto_notas)
        pdf.ln(th)
        pdf.ln(th)
        
        text_compromisso_honra='Eu, ' + str(row[1]) + ' Product Leader de ' +  str(row[4]) + ' confirmo, sob compromisso de honra, que a pessoa mencionada tomou conhecimento da presente avaliação.'   
        pdf.multi_cell(0, 5, text_compromisso_honra)
        pdf.ln(th)  
        pdf.ln(th)  

        pdf.cell(page_width, th,'Data: '+ str(row[39]), align='C')

        return Response(pdf.output(dest='S'), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=Avaliação '+str(row[4])+'.pdf'})

@app.route('/table_team_leader_extra_pl/<int:id>')
def table_team_leader_extra_pl(id):

    con=conn2.cursor()
    con.execute('SELECT * FROM tlquest WHERE id = {0}' .format(id))  
    minha_avaliacao=con.fetchall()
    con.close()
    today = date.today()

    for row in minha_avaliacao:
        # Make a PDF straight from HTML in a string.
        pdf = FPDF()

        pdf = FPDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True,margin = 20)
       
        
        page_width = pdf.w - 2 * pdf.l_margin
        print (page_width)
        pdf.set_font('Times','B',16) 
        pdf.cell(190, 0.0, 'Avaliação: '+ str(row[4]), align='R')
        pdf.ln(6)
        pdf.cell(190, 0.0, 'Motivo: '+ str(row[44]), align='R')
        pdf.image("static/content/BorgWarner_Technology_Blue.png", 10,10,80,10)
        pdf.set_font('Times', '', 14)
        
        col_width = page_width/2
        col_width_small = page_width/4
             
        pdf.ln(1)
             
        th = pdf.font_size
     
        pdf.ln(10)

        pdf.cell(60, th, 'Data: '+ str(row[3]), border=0)
        pdf.cell(70, th, 'Colaborador/a: '+ str(row[4]), border=0)
        pdf.cell(60, th, 'Product Leader: '+ str(row[1]), border=0)
        pdf.ln(10)
        pdf.set_font('Times','B',14) 
        pdf.cell(col_width_small, th, 'Cultura e Segurança', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 11)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[6]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[26]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',14) 
        pdf.cell(col_width_small, th, 'Orientação Qualidade', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 11)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[8]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[26]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',14) 
        pdf.cell(col_width_small, th, 'Orientação Resultados', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 11)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[10]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[27]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',14) 
        pdf.cell(col_width_small, th, 'Relacionamento Interpessoal', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 11)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[12]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[28]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',14) 
        pdf.cell(col_width_small, th, 'Trabalho Equipa', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 11)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[14]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[29]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',14) 
        pdf.cell(col_width_small, th, 'Competências Técnicas/Funcionais', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 11)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[16]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[30]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',14) 
        pdf.cell(col_width_small, th, 'Gestão Equipa', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 11)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[18]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[31]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',14) 
        pdf.cell(col_width_small, th, 'Pontualidade', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 11)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[20]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[32]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',14) 
        pdf.cell(col_width_small, th, 'Assiduidade', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 11)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[22]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[33]), border=0)
        pdf.ln(8)

        pdf.set_font('Times','B',14) 
        pdf.cell(col_width_small, th, 'Apreciação Global', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 11)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[24]), border=0)
        pdf.ln(5)
        pdf.cell(col_width_small, th, 'Comentário: ' +str(row[34]), border=0)
        pdf.ln(8)



        
        pdf.set_font('Times','B',14) 
        pdf.cell(col_width_small, th, 'Avaliação final', border=0)
        pdf.ln(8)
        pdf.set_font('Times', '', 11)
        pdf.cell(col_width_small, th, 'Nota: ' +str(row[38]), border=0)

        pdf.ln(8)
    
 
        #pdf.set_font('Times','',14.0)
        #texto_notas='Notas: '+str(row[34])
        #pdf.cell(page_width, th,'Notas: ' +str(row[34]))
        #pdf.multi_cell(0, 5, texto_notas)
        #pdf.ln(th)
        pdf.set_font('Times','',11)
        text_compromisso_honra='Eu, ' + str(row[1]) + ' Product Leader do colaborador/a,  ' +  str(row[4]) + ' realizei esta avaliação extraordinária pelo motivo - "'+ str(row[44])+'" .'   
        pdf.multi_cell(0, 5, text_compromisso_honra)

        return Response(pdf.output(dest='S'), mimetype='application/pdf', headers={'Content-Disposition':'attachment;filename=avaliacao_'+str(row[4])+'.pdf'}) 


if __name__ == "__main__":
    app.run(debug=True)

