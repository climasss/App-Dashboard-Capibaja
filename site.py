import streamlit as st

# Configuração da página em modo Wide para controle das margens
st.set_page_config(page_title="Hub Capibaja Nacional 2026", layout="wide")

# --- SISTEMA DE MARGENS ---
# Criamos 3 colunas: as das pontas servem como margens vazias.
col_lateral_esq, col_central, col_lateral_dir = st.columns([4, 4, 4])

# Deixamos a lateral esquerda vazia
with col_lateral_esq:
    st.empty()

# --- CONTEÚDO CENTRAL ---
with col_central:
    st.title("Hub de informações Nacional 2026 - CapiBaja")
    st.markdown("---")

    # --- REGULAMENTO ---
    st.write("### 📄 Regulamento Nacional 2026")
    st.link_button(
        label = "RATBSB emenda 07",
        url="https://arquivos.saebrasil.org.br/2026/BajaNacional/RATBSB_emenda_07.pdf",
        use_container_width=True,
    )
    st.markdown("---")

    # --- LOCALIZAÇÃO DO HOTEL (NOVO) ---
    st.write("### 📍 Localização do Hotel")
    st.link_button(
        label = "Ver no Google Maps",
        url="https://maps.google.com/maps/place/Plaza+Hotel+São+Jose+dos+Campos+SJC/data=!4m2!3m1!1s0x0:0x8b32f9c1a59984a1?sa=X&ved=1t:2428&ictx=111", # Certifique-se de que este link está correto
        use_container_width=True,
    )
    st.markdown("---")

    # --- DRIVE ---
    st.write("### 📁 Drive da equipe")
    st.link_button(
        label = "Drive",
        url="https://drive.google.com/drive/u/2/folders/0AN6vqF3uDEnpUk9PVA",
        use_container_width=True,
    )
    st.markdown("---")

    # --- GITHUB ---
    st.write("### ⚡Github da elétrica Capibaja")
    st.link_button(
        label = "Git da Equipe",
        url="https://github.com/Capibaja",
        use_container_width=True,
    )
    st.markdown("---")

    # --- EXCEL BAJA ---
    st.write("### 📊Excel Baja")
    st.link_button(
        label = "excel",
        url="https://excelbaja.streamlit.app/",
        use_container_width=True,
    )
    st.subheader("🛠️ Como Usar:")
    st.write("1. Jogar a planilha de dados LoRa ao entrar no site.")
    st.write("2. Selecionar o tipo de gráfico desejado.")
    st.write("3. Selecionar as variáveis no eixo X e eixo Y.")
    st.write("4. Clique em 'Gerar Gráfico'.")
    st.write("5. Baixe o html do gráfico para deixar salvo.")
    st.markdown("---")

    # --- DOWNLOAD EXECUTÁVEL ---
    st.write("### 📥 Versão de Telemetria (Executável)")
    link_do_drive = "https://drive.google.com/file/d/1FBRJhkp5cuMBoaAkVPEDiBnyB6nfp1VL/view?usp=drive_link"

    st.link_button(
        label="🚀 Baixar Monitor Serial (.exe)",
        url=link_do_drive,
        use_container_width=True,
        help="Clique para ser redirecionado ao download no Google Drive."
    )
    st.subheader("🛠️ Como instalar:")
    st.write("1. Clique no botão acima e baixe o arquivo.")
    st.write("2. Se o Windows avisar que o arquivo é 'inseguro', clique em **Mais informações** e **Executar assim mesmo**.")
    st.markdown("---")

# Deixamos a lateral direita vazia
with col_lateral_dir:
    st.empty()
