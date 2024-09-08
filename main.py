import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Predição de Doenças Cardíacas",
    page_icon=":heart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """<div style='text-align: left;'><h2>Bem vindo, a ferramenta de predição de doenças cardíacas!</h2></div>""",
    unsafe_allow_html=True)
st.write("#####")

texto_1 = """
<p style='text-align: justify;'>
Oferecer uma ferramenta preditiva capaz de auxiliar médicos e pacientes na detecção precoce de doenças cardíacas, utilizando Inteligência Artificial. Desenvolvida com base em algoritmos de machine learning, ela analisa dados médicos detalhados para fornecer um pré-diagnóstico confiável e eficiente.
</p>
"""

texto_2 = """
<p style='text-align: justify;'>
A ferramenta processa informações como idade, nível de colesterol, pressão arterial e outros indicadores clínicos, identificando padrões que podem indicar riscos cardíacos. Isso permite que a saúde do coração seja monitorada de forma rápida e assertiva, mesmo em estágios iniciais, quando as chances de prevenção e tratamento eficaz são maiores.
</p>
"""

texto_3 = """
<p style='text-align: justify;'>
Com uma interface simples e intuitiva, os usuários podem inserir seus dados clínicos e obter uma análise imediata dos possíveis riscos cardíacos. Combinando tecnologia com facilidade de uso, nossa ferramenta não só auxilia os profissionais de saúde no diagnóstico, mas também permite que qualquer pessoa monitore sua saúde cardíaca de forma precisa e descomplicada.

Experimente a ferramenta e veja como a Inteligência Artificial pode transformar o futuro do diagnóstico cardiovascular.
</p>
"""

#A ferramenta foi projetada para ser intuitiva e acessível, permitindo que profissionais da saúde insiram dados dos pacientes e obtenham rapidamente uma previsão sobre a probabilidade de doenças cardíacas. Com isso, espera-se contribuir para a melhoria dos cuidados médicos e a redução de complicações decorrentes de diagnósticos tardios.

# CRIANDO ESTADOS
if 'condicao_gerar' not in st.session_state:
    st.session_state['condicao_gerar'] = False

# -- INTRODUÇÃO --
col1, col2, col3 = st.columns([0.4, 2, 0.4])
with col2:

    with st.container():
        st.markdown(
            """<div style='text-align: center;'><h3>INTRODUÇÃO</h3></div>""",
            unsafe_allow_html=True)
        st.write("#####")
        st.write("**Nossa proposta**")
        st.markdown(texto_1, unsafe_allow_html=True)
        st.write("")
        st.write("**Como ela funciona?**")
        st.markdown(texto_2, unsafe_allow_html=True)
        st.write("")
        st.write("**Interface**")
        st.markdown(texto_3, unsafe_allow_html=True)

st.write("---")

if st.session_state['condicao_gerar'] == False:

    st.markdown(
        """<div style='text-align: center;'><h4>INFORMAÇÕES PARA PRÉ-DIAGNÓSTICO</h4></div>""",
        unsafe_allow_html=True)
    st.write("#####")

    col1, col2, col3 = st.columns([0.2, 2, 0.2])
    with col2:
        with st.container(border=True):
            st.write("Preencha todas as informações:")
            col1, col2, col3 = st.columns(3)

            with col1:

                #st.write("#####")

                st.markdown(
                    """<div style='text-align: center;'><h5>Informações Básicas</h5></div>""",
                    unsafe_allow_html=True)

                st.session_state['nome'] = st.text_input("Nome:")
                email = st.text_input("E-Mail:")
                idade = st.number_input("Idade:", format="%0.0f")
                sexo = dor_peito = st.selectbox(
                    "Sexo:",
                    ("Masculino", "Feminino"),
                )

                dor_peito = st.selectbox(
                    "Tipo de dor no peito:",
                    ("ATA", "NAP", "TA", "Não tenho"),
                )

            with col2:
                st.markdown(
                    """<div style='text-align: center;'><h5>Exame de sangue</h5></div>""",
                    unsafe_allow_html=True)

                colestol = st.number_input("Colesterol LDL:", format="%0.2f")
                glicemia_jejum = st.number_input("Glicemia em jejum:",
                                                 format="%0.2f")

            with col3:
                st.markdown(
                    """<div style='text-align: center;'><h5>Exame do coração</h5></div>""",
                    unsafe_allow_html=True)

                pressao_arterial = st.number_input(
                    "Pressão arterial em repouso:", format="%0.2f")
                eletrocardiograma = st.number_input(
                    "Resultado do eletrocardiograma em repouso:",
                    format="%0.2f")
                frequencia_card = st.number_input(
                    "Frequência cardíaca máxima atingida :", format="%0.2f")
                angina_exercicio = st.number_input(
                    "Angina induzida por exercício:", format="%0.2f")
                insuficiencia_card = st.number_input(
                    "Insuficiência do fluxo sanguíneo para o músculo cardíaco:",
                    format="%0.2f")
                padrao_ecg = st.number_input("Padrão ECG :", format="%0.2f")

        if st.button("Gerar pré-diagnostico"):
            st.session_state['condicao_gerar'] = True
            st.rerun()

# EXIBINDO RESULTADO
else:
    
    st.write("#####")


    col1, col2, col3 = st.columns(3)
    with col2:

        with st.container():

            st.image("—Pngtree—vector alert icon_3767407.png", use_column_width=True)

            st.markdown("""<div style='text-align: center;'>
                   <h1 style='color: #c92020;'>77% de chance</h1>
               </div>""",
                    unsafe_allow_html=True)

            st.write("")
            st.markdown(
                """<div style='text-align: center;'><h5>RECOMENDAÇÃO</h5></div>""",
                unsafe_allow_html=True)
    
            recomendacao = """
            <p style='text-align: justify;'>
            É recomendado ter um acompanhamento de um médico cardiologista, tendo uma melhora na alimentação, e praticando atividade física
            </p>
            """
            st.markdown(recomendacao, unsafe_allow_html=True)
       
            st.markdown(
                """<div style='text-align: left;'>
                       <p>Agende uma consulta através do <a href='https://meususdigital.saude.gov.br/consultas'>link</a></p>
                   </div>""",
                unsafe_allow_html=True
            )

    
            
            


        if st.button("Voltar para gerador"):
            st.session_state['condicao_gerar'] = False
            st.rerun()
        
        nome = st.session_state['nome']
        st.write(nome)
    