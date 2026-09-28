import io
import pandas as pd
import plotly.io as pio

pio.templates.default = "plotly"

def tabela_para_csv(df: pd.DataFrame) -> bytes:
  
    return df.to_csv(index=False).encode("utf-8-sig")

def tabela_para_excel(df: pd.DataFrame) -> bytes:
    
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Frequência")
    return buffer.getvalue()

def grafico_para_png(fig, escala: int = 2) -> bytes:
  
    return fig.to_image(format="png", scale=escala)