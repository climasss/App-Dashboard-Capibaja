import streamlit as st

# Configuração da página em modo Wide para controle das margens
st.set_page_config(page_title="Hub Capibaja Nacional 2026", layout="wide")

# --- SISTEMA DE MARGENS ---
# Criamos 3 colunas: as das pontas servem como margens vazias.
col_lateral_esq, col_central, col_lateral_dir = st.columns([4, 4, 4])

# Deixamos a lateral esquerda vazia
with col_lateral_esq:
    st.markdown('<h1 style="text-align: center;">Cronograma</h1>', unsafe_allow_html=True)

    # Quarta
    st.markdown("""
    <div style="border-left: 5px solid #4CAF50; padding-left: 15px; margin-bottom: 20px;">
        <h3>Quarta – 25 de Março de 2026</h3>
        <p>• Credenciamento – 08:00 às 17:30</p>
    </div>
    """, unsafe_allow_html=True)

    # Quinta
    st.markdown("""
    <div style="border-left: 5px solid #2196F3; padding-left: 15px; margin-bottom: 20px;">
        <h3>Quinta – 26 de Março de 2026</h3>
        <p>• Inspeção de Conformidade Técnica e Segurança – 08:00 às 18:00</p>
        <p>• Apresentação de Projeto Dinâmico / Segurança Dinâmica – 09:00 às 18:00</p>
    </div>
    """, unsafe_allow_html=True)

    # Sexta
    st.markdown("""
    <div style="border-left: 5px solid #9C27B0; padding-left: 15px; margin-bottom: 20px;">
        <h3>Sexta – 27 de Março de 2026</h3>
        <p>• Inspeção de Conformidade Técnica e Segurança – 08:00 às 18:00</p>
        <p>• Apresentação de Projeto Dinâmico / Segurança Dinâmica – 08:00 às 18:00</p>
        <p>• Apresentação de Projeto Núcleo Técnico – 08:00 às 16:20</p>
        <p>• Apresentação de Projeto Núcleo de Negócios – 08:00 às 15:45</p>
        <p>• Feedback de Projeto – 17:00 às 18:00</p>
    </div>
    """, unsafe_allow_html=True)

    # Sábado
    st.markdown("""
    <div style="border-left: 5px solid #FF9800; padding-left: 15px; margin-bottom: 20px;">
        <h3>Sábado – 28 de Março de 2026</h3>
        <p>• Inspeção de Conformidade Técnica e Segurança – 08:00 às 13:00</p>
        <p>• Apresentação de Projeto Dinâmico / Segurança Dinâmica – 08:00 às 14:00</p>
        <p>• Finais de Projeto – 08:00 às 09:30</p>
        <p>• Dinâmicas Janela Aberta – 10:00 às 14:00</p>
        <p>• Super Prime – 15:00 às 17:30</p>
    </div>
    """, unsafe_allow_html=True)

    # Domingo
    st.markdown("""
    <div style="border-left: 5px solid #F44336; padding-left: 15px; margin-bottom: 20px;">
        <h3>Domingo – 29 de Março de 2026</h3>
        <p>• Reconhecimento de pista somente com os pilotos – 08:00 às 08:30</p>
        <p>• Formação do GRID – 09:10 às 09:40</p>
        <p>• Vide janelas no site de pontuação!!</p>
        <p>• Enduro de Resistência – 10:00 às 14:00</p>
        <p>• Premiação – 15:00 às 16:30</p>
    </div>
    """, unsafe_allow_html=True)

# --- CONTEÚDO CENTRAL ---
with col_central:
    st.markdown('<h1 style="text-align: center;">Hub de informações Nacional 2026 - CapiBaja</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # --- REGULAMENTO ---
    st.markdown("""
    <h3 style="text-align: center; margin-bottom: 5px;">
    📄 Regulamento Nacional 2026
    </h3>
    """, unsafe_allow_html=True)

    st.link_button(
        label="RATBSB emenda 07",
        url="https://arquivos.saebrasil.org.br/2026/BajaNacional/RATBSB_emenda_07.pdf",
        use_container_width=True,
    )

    st.markdown("---")

    # --- RESULTADOS ---
    st.markdown("""
    <h3 style="text-align: center; margin-bottom: 5px;">
    🌐 Resultados Baja SAE Brasil
    </h3>
    """, unsafe_allow_html=True)

    st.link_button(
        label="Ver Resultados",
        url="https://resultados.bajasaebrasil.net/",
        use_container_width=True,
    )

    st.markdown("---")

    # --- FILA ICTS ---
    st.markdown("""
    <h3 style="text-align: center; margin-bottom: 5px;">
    👨‍⚕️🚑🏥 Fila ICTS
    </h3>
    """, unsafe_allow_html=True)

    st.link_button(
        label="Ver Fila",
        url="https://fila.bajasaebrasil.net/fila.php?evento=26BR&fila=2",
        use_container_width=True,
    )

    st.markdown("---")

    # --- LOCALIZAÇÃO ---
    st.markdown("""
    <h3 style="text-align: center; margin-bottom: 5px;">
    📍 Localização do Hotel
    </h3>
    """, unsafe_allow_html=True)

    st.link_button(
        label="Ver no Google Maps",
        url="https://maps.google.com/maps/place/Plaza+Hotel+São+Jose+dos+Campos+SJC/data=!4m2!3m1!1s0x0:0x8b32f9c1a59984a1?sa=X&ved=1t:2428&ictx=111",
        use_container_width=True,
    )

    st.markdown("---")

    # --- DRIVE ---
    st.markdown("""
    <h3 style="text-align: center; margin-bottom: 5px;">
    📁 Drive da equipe
    </h3>
    """, unsafe_allow_html=True)

    st.link_button(
        label="Drive",
        url="https://drive.google.com/drive/u/2/folders/0AN6vqF3uDEnpUk9PVA",
        use_container_width=True,
    )

    st.markdown("---")

    # --- GITHUB ---
    st.markdown("""
    <h3 style="text-align: center; margin-bottom: 5px;">
    ⚡ Github da elétrica Capibaja
    </h3>
    """, unsafe_allow_html=True)

    st.link_button(
        label="Git da Equipe",
        url="https://github.com/Capibaja",
        use_container_width=True,
    )

    st.markdown("---")

    # --- EXCEL ---
    st.markdown("""
    <h3 style="text-align: center; margin-bottom: 5px;">
    📊 Excel Baja
    </h3>
    """, unsafe_allow_html=True)

    st.link_button(
        label="Excel",
        url="https://excelbaja.streamlit.app/",
        use_container_width=True,
    )

    st.markdown("""
    <h4 style="text-align: center; margin-top: 15px;">
    🛠️ Como Usar:
    </h4>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align: center;">
    1. Jogar a planilha de dados LoRa ao entrar no site.<br>
    2. Selecionar o tipo de gráfico desejado.<br>
    3. Selecionar as variáveis no eixo X e eixo Y.<br>
    4. Clique em 'Gerar Gráfico'.<br>
    5. Baixe o html do gráfico para deixar salvo.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")
    link_do_drive = "https://drive.google.com/file/d/1FBRJhkp5cuMBoaAkVPEDiBnyB6nfp1VL/view?usp=drive_link"
    
    st.markdown("""
    <h3 style="text-align: center; margin-bottom: 5px;">
    📊 Dashboard Telemetria
    </h3>
    """, unsafe_allow_html=True)
    
    st.link_button(
    label="🚀 Baixar Monitor Serial (.exe)",
    url=link_do_drive,
    use_container_width=True,
    help="Clique para ser redirecionado ao download no Google Drive."
    )

    st.markdown("""
    <h4 style="text-align: center; margin-top: 15px;">
    🛠️ Como Instalar:
    </h4>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="text-align: center;">
    1. Clique no botão acima e baixe o arquivo.<br>
    2. Se o Windows avisar que o arquivo é 'inseguro', clique em **Mais informações** e **Executar assim mesmo**.<br>
    """, unsafe_allow_html=True)

# Deixamos a lateral direita vazia
with col_lateral_dir:
    st.markdown('<h1 style="text-align: center;">Voluntários</h1>', unsafe_allow_html=True)

    # Comitê Técnico – Azul Royal
    st.markdown("""
    <div style="border-right: 5px solid #4169E1; padding-right: 15px; margin-bottom: 15px; text-align: right;">
        <h3>Comitê Técnico</h3>
        <p>• Camiseta: Azul Royal</p>
    </div>
    """, unsafe_allow_html=True)

    # Juiz – Amarelo Ouro
    st.markdown("""
    <div style="border-right: 5px solid #FFD700; padding-right: 15px; margin-bottom: 15px; text-align: right;">
        <h3>Juiz</h3>
        <p>• Camiseta: Amarelo Ouro</p>
    </div>
    """, unsafe_allow_html=True)

    # Assessor técnico – Verde Bandeira
    st.markdown("""
    <div style="border-right: 5px solid #009B3A; padding-right: 15px; margin-bottom: 15px; text-align: right;">
        <h3>Assessor Técnico</h3>
        <p>• Camiseta: Verde Bandeira</p>
    </div>
    """, unsafe_allow_html=True)

    # Comissão – Rosa
    st.markdown("""
    <div style="border-right: 5px solid #FF69B4; padding-right: 15px; margin-bottom: 15px; text-align: right;">
        <h3>Comissão</h3>
        <p>• Camiseta: Rosa (Verde no Enduro)</p>
    </div>
    """, unsafe_allow_html=True)

    # Staff – Amarelo Bebê
    st.markdown("""
    <div style="border-right: 5px solid #FFFACD; padding-right: 15px; margin-bottom: 15px; text-align: right;">
        <h3>Staff</h3>
        <p>• Camiseta: Amarelo Bebê</p>
    </div>
    """, unsafe_allow_html=True)

    # Segurança – Vermelho
    st.markdown("""
    <div style="border-right: 5px solid #FF0000; padding-right: 15px; margin-bottom: 15px; text-align: right;">
        <h3>Segurança</h3>
        <p>• Camiseta: Vermelho</p>
    </div>
    """, unsafe_allow_html=True)

    # Imprensa – Laranja
    st.markdown("""
    <div style="border-right: 5px solid ##FF5C00; padding-right: 15px; margin-bottom: 15px; text-align: right;">
        <h3>Imprensa</h3>
        <p>• Colete: Laranja</p>
    </div>
    """, unsafe_allow_html=True)

    # Apoio de pista – Vermelho (tom mais escuro)
    st.markdown("""
    <div style="border-right: 5px solid #8B0000; padding-right: 15px; margin-bottom: 15px; text-align: right;">
        <h3>Apoio de pista</h3>
        <p>• Colete: Vermelho</p>
    </div>
    """, unsafe_allow_html=True)
