import streamlit as st
import pandas as pd
import plotly.express as px


from dados_exemplo import listar_datasets, obter_dataset
from exportar import tabela_para_csv, tabela_para_excel, grafico_para_png


@st.cache_data(show_spinner=False)
def _gerar_png_cache(_fig, chave_dados, nome_grafico, escala=2):
    return grafico_para_png(_fig, escala)


st.set_page_config(page_title="Análise Qualitativa", page_icon="📊", layout="wide")


st.title("📊 Análise de Dados Qualitativos")
st.markdown("Gere tabelas de frequência e gráficos interativos para dados nominais ou ordinais.")


with st.sidebar:
    st.header("Entrada de Dados")
    st.write("Insira os seus dados qualitativos abaixo, separados por vírgula.")

    
    dados_padrao = "Masculino, Feminino, Feminino, Masculino, Outro, Feminino, Masculino, Feminino"

  
    exemplo_escolhido = st.selectbox("Ou carregue um exemplo pronto:", ["Nenhum"] + listar_datasets())
    if exemplo_escolhido != "Nenhum":
        dados_padrao = obter_dataset(exemplo_escolhido)
   

    entrada_texto = st.text_area("Dados:", value=dados_padrao, height=150)

    st.info("💡 **Dica:** Pode colar colunas de dados aqui, apenas certifique-se de os separar por vírgulas.")


if entrada_texto:
    lista_dados = [item.strip().title() for item in entrada_texto.split(",") if item.strip() != ""]

    if len(lista_dados) > 0:
        df = pd.DataFrame(lista_dados, columns=['Categoria'])

        freq_absoluta = df['Categoria'].value_counts().reset_index()
        freq_absoluta.columns = ['Categoria', 'Frequência Absoluta']

        freq_relativa = df['Categoria'].value_counts(normalize=True).reset_index()
        freq_relativa.columns = ['Categoria', 'Frequência Relativa (%)']
        freq_relativa['Frequência Relativa (%)'] = (freq_relativa['Frequência Relativa (%)'] * 100).round(2)

        tabela_resumo = pd.merge(freq_absoluta, freq_relativa, on='Categoria')

        st.divider()

        
        st.subheader("📋 Tabelas de Frequência")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Frequência Absoluta e Relativa**")
            st.dataframe(tabela_resumo, width='stretch', hide_index=True)

            
            col_csv, col_xlsx = st.columns(2)
            with col_csv:
                st.download_button(
                    "⬇️ CSV", tabela_para_csv(tabela_resumo),
                    "tabela_frequencia.csv", "text/csv"
                )
            with col_xlsx:
                st.download_button(
                    "⬇️ Excel", tabela_para_excel(tabela_resumo),
                    "tabela_frequencia.xlsx",
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            

        with col2:
            st.markdown("**Métricas Gerais**")
            st.metric("Total de Observações (N)", len(lista_dados))
            st.metric("Categorias Únicas", len(tabela_resumo))

        st.divider()

        st.subheader("📈 Gráficos Qualitativos")
        col_graf1, col_graf2 = st.columns(2)

        with col_graf1:
            fig_bar = px.bar(
                tabela_resumo, x='Categoria', y='Frequência Absoluta',
                text='Frequência Absoluta', color='Categoria', title='Gráfico de Barras'
            )
            fig_bar.update_traces(textposition='outside')
            fig_bar.update_layout(showlegend=False)
            st.plotly_chart(fig_bar, width='stretch')

            
           

        with col_graf2:
            fig_pie = px.pie(
                tabela_resumo, names='Categoria', values='Frequência Absoluta',
                title='Gráfico de Setores (Pizza)', hole=0.3
            )
            fig_pie.update_traces(textinfo='percent+label')
            st.plotly_chart(fig_pie, width='stretch')

        
            
    else:
        st.warning("Por favor, insira pelo menos um dado válido.")