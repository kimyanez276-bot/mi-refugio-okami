import streamlit as st
import time

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="💖 Mi Refugio | Okami & Sakura", page_icon="🌸", layout="centered")

# --- ESTILOS CSS CON MÁXIMO CONTRASTE Y CORRECCIÓN DE EXPANDERS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap');
    
    .stApp {
        background-color: #0B0B0F !important;
    }
    
    html, body, [class*="st"] {
        font-family: 'Quicksand', sans-serif;
        color: #FFFFFF !important;
    }
    
    h1 {
        color: #FFB7C5 !important;
        text-align: center;
        font-weight: 700;
        text-shadow: 0 2px 10px rgba(255, 183, 197, 0.4);
    }

    h2, h3 {
        color: #FFD1DC !important;
        font-weight: 700;
    }

    /* Tarjetas y Post-its estilo mágico */
    .card {
        padding: 25px;
        border-radius: 20px;
        background-color: #171721;
        box-shadow: 0 8px 25px rgba(255, 183, 197, 0.2);
        margin-bottom: 20px;
        border: 2px solid rgba(255, 183, 197, 0.4);
    }
    
    /* Botones personalizados estilo mágico */
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 3.2em;
        font-weight: 600;
        font-size: 1.05em;
        border: none;
        background-color: #FFB7C5 !important;
        color: #0B0B0F !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(255,183,197,0.3);
    }
    
    .stButton>button:hover {
        background-color: #FF99A6 !important;
        color: white !important;
    }

    /* Textos generales y párrafos con color blanco nítido */
    p, span, label, .stMarkdown, div {
        color: #FFFFFF !important;
    }

    /* Corrección visual para los desplegables (Expanders) en móvil */
    .streamlit-expanderHeader {
        background-color: #171721 !important;
        color: #FFB7C5 !important;
        border-radius: 10px;
        border: 1px solid rgba(255, 183, 197, 0.3);
    }

    /* Inputs y selectores */
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stTextArea>div>div>textarea {
        background-color: #171721 !important;
        color: #FFFFFF !important;
        border: 1px solid #FFB7C5 !important;
    }

    .firma {
        text-align: center;
        color: #A0A0B0;
        font-size: 0.85em;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# --- BANNER MÁGICO SUPERIOR (Okami y Cerezos) ---
st.image("Gemini_Generated_Image_sez74ssez74ssez7.jpg", use_container_width=True)

# --- ESTRUCTURA DE LA APP ---
st.markdown("<h1>💖 Tu Espacio Protegido</h1>", unsafe_allow_html=True)
st.markdown("""
    <div style="text-align:center; font-size: 1.15em; margin-bottom: 25px; color: #FFFFFF !important;">
        Respira profundamente. Aquí no hay prisas ni culpas. 
        Este es tu santuario mágico para organizar tu trabajo, tu hogar y tu bienestar, 
        protegida por la magia de los cerezos y tu fiel compañero 
        <span style="font-weight: 700; color: #FFB7C5;">Okami</span>. 🌸✨
    </div>
""", unsafe_allow_html=True)

# Inicializar listas de tareas en session_state si no existen
if 'tarjetas' not in st.session_state:
    st.session_state.tarjetas = [
        {"cat": "💼 Trabajo", "texto": "Calcular IVA y revisar F29"},
        {"cat": "🏠 Casa", "texto": "Ordenar la sala y preparar ropa de mañana"},
        {"cat": "🧘‍♀️ Salud", "texto": "Tomar agua y vitaminas / 10 min de pausa"},
        {"cat": "💰 Economía", "texto": "Revisar avances de Divina Pisada"}
    ]

# Inicializar Procesos / Post-its de Trabajo en session_state si no existen
if 'procesos' not in st.session_state:
    st.session_state.procesos = [
        {"titulo": "📌 Cierre / Cálculo de IVA", "pasos": "1. Revisar Registro de Compras y Ventas en el SII.\n2. Verificar Remanente de Crédito Fiscal.\n3. Calcular débito y crédito fiscal (F29)."},
        {"titulo": "📌 Liquidaciones y Remuneraciones", "pasos": "1. Verificar novedades de asistencia.\n2. Correr modelo en Python/Excel.\n3. Validar cotizaciones (AFP, Salud, CCAF)."}
    ]

# 1. Semáforo de Energía Matutino (Opcional)
if 'energia' not in st.session_state:
    st.session_state.energia = None

if st.session_state.energia is None:
    st.markdown("---")
    st.markdown("### ☀️ ¿Cómo está tu energía hoy? (Opcional)")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        if st.button("🔴 Baja"):
            st.session_state.energia = "Baja"
            st.rerun()
    with col2:
        if st.button("🟡 Media"):
            st.session_state.energia = "Media"
            st.rerun()
    with col3:
        if st.button("🟢 Alta"):
            st.session_state.energia = "Alta"
            st.rerun()
    with col4:
        if st.button("⏭️ Saltar"):
            st.session_state.energia = "Omitido"
            st.rerun()
else:
    if st.session_state.energia != "Omitido":
        st.success(f"Energía configurada para hoy: **{st.session_state.energia}**. ¡A tu propio ritmo, todo está bien!")
    
    if st.button("🔄 Cambiar / Ocultar energía de hoy"):
        st.session_state.energia = None
        st.rerun()

# Menú Principal de Categorías
st.markdown("---")
st.subheader("🌸 Elige qué sección quieres visitar hoy:")
menu = st.radio("Opciones", [
    "🃏 Tarjetas Mágicas", 
    "📝 Crear y Ver Mis Listas", 
    "⏱️ Cronómetro / Foco", 
    "📋 Procesos de Trabajo", 
    "✨ Registro de Victorias"
], label_visibility="collapsed")

# SECCIÓN 1: TARJETAS (ESTILO TINDER / CARTAS CLOW)
if menu == "🃏 Tarjetas Mágicas":
    st.subheader("🎯 Tus Pendientes del Día")
    st.write("Desliza o decide qué carta activar a continuación:")

    if st.session_state.tarjetas:
        tarjeta_actual = st.session_state.tarjetas[0]
        
        st.markdown(f"""
            <div class="card">
                <h3 style="color: #FFB7C5 !important; font-size: 1.5em;">{tarjeta_actual['cat']}</h3>
                <p style="font-size: 1.3em; margin-top: 15px; color: #FFFFFF !important;">{tarjeta_actual['texto']}</p>
            </div>
        """, unsafe_allow_html=True)

        col_izq, col_der = st.columns(2)
        with col_izq:
            if st.button("❌ Posponer / Después"):
                st.session_state.tarjetas.append(st.session_state.tarjetas.pop(0))
                st.rerun()
        with col_der:
            if st.button("❤️ ¡Hecho! (¡Liberado!)"):
                completada = st.session_state.tarjetas.pop(0)
                st.balloons()
                st.success(f"¡Magia pura! Tachaste: '{completada['texto']}' 🎉")
                st.rerun()
    else:
        st.success("🎉 ¡Increíble! Has liberado todas tus cartas pendientes por hoy. ¡Descansa y celebra!")

# SECCIÓN 2: CREAR Y VER TODAS TUS LISTAS AGRUPADAS (TODOS LOS OBJETIVOS JUNTOS)
elif menu == "📝 Crear y Ver Mis Listas":
    st.subheader("📝 Panel General: Todas tus Listas y Objetivos")
    st.write("Aquí puedes agregar nuevas tareas y ver **todos tus objetivos juntos** agrupados por categoría:")
    
    with st.form("nueva_tarea_form"):
        cat_nueva = st.selectbox("Categoría:", ["💼 Trabajo", "🏠 Casa", "🧘‍♀️ Salud", "💰 Economía", "✨ Personal"])
        texto_nuevo = st.text_input("¿Qué tarea u objetivo quieres agregar?")
        btn_agregar = st.form_submit_button("✨ Añadir a mis listas")
        
        if btn_agregar and texto_nuevo:
            st.session_state.tarjetas.append({"cat": cat_nueva, "texto": texto_nuevo})
            st.success(f"¡Guardado en {cat_nueva} con éxito!")
            st.rerun()

    st.markdown("---")
    st.subheader("📂 Tus Objetivos Agrupados por Categoría")
    
    if st.session_state.tarjetas:
        categorias_unicas = set(t['cat'] for t in st.session_state.tarjetas)
        for cat in sorted(categorias_unicas):
            st.markdown(f"### {cat}")
            for i, t in enumerate(st.session_state.tarjetas):
                if t['cat'] == cat:
                    col_t, col_b = st.columns([4, 1])
                    with col_t:
                        st.markdown(f"- {t['texto']}")
                    with col_b:
                        if st.button("🗑️", key=f"del_{cat}_{i}"):
                            st.session_state.tarjetas.pop(i)
                            st.rerun()
            st.markdown("")
    else:
        st.info("No tienes tareas pendientes guardadas en este momento. ¡Agrega una arriba!")

# SECCIÓN 3: CRONÓMETRO / FOCO
elif menu == "⏱️ Cronómetro / Foco":
    st.subheader("⏱️ Tu Zona de Concentración Mágica")
    st.write("Elige cuántos minutos quieres dedicarle a una tarea sin distracciones:")
    
    minutos = st.slider("Minutos de foco:", 5, 45, 25)
    if st.button("🚀 ¡Activar Sello de Foco!"):
        with st.status("⏳ Canalizando energía... ¡Tú puedes!", expanded=True) as status:
            bar = st.progress(0)
            for i in range(minutos):
                time.sleep(1)
                bar.progress((i + 1) / minutos)
            status.update(label="¡Tiempo cumplido! Sello liberado. Tómate un descanso bajo los cerezos. 🌸", state="complete", expanded=True)
            st.balloons()

# SECCIÓN 4: PROCESOS DE TRABAJO (AHORA EDITABLES COMO POST-ITS)
elif menu == "📋 Procesos de Trabajo":
    st.subheader("📋 Tus Guías y Pasos Fijos (Post-its Editables)")
    st.write("Crea y edita tus propias fórmulas y pasos para que tu mente descanse:")
    
    # Formulario para agregar nuevo post-it de proceso
    with st.form("nuevo_proceso_form"):
        titulo_p = st.text_input("Título del Proceso (ej. 📌 Cierre F29):")
        pasos_p = st.text_area("Pasos (escribe cada paso en una línea):")
        btn_crear_p = st.form_submit_button("✨ Crear Nuevo Post-it")
        
        if btn_crear_p and titulo_p and pasos_p:
            st.session_state.procesos.append({"titulo": titulo_p, "pasos": pasos_p})
            st.success("¡Post-it de proceso guardado con éxito!")
            st.rerun()

    st.markdown("---")
    st.subheader("📌 Tus Post-its Guardados")
    
    if st.session_state.procesos:
        for idx, proc in enumerate(st.session_state.procesos):
            with st.expander(proc['titulo']):
                st.markdown(f"<div style='white-space: pre-wrap;'>{proc['pasos']}</div>", unsafe_allow_html=True)
                if st.button("🗑️ Eliminar este post-it", key=f"del_proc_{idx}"):
                    st.session_state.procesos.pop(idx)
                    st.rerun()
    else:
        st.info("No tienes procesos guardados todavía. ¡Crea uno arriba!")

# SECCIÓN 5: REGISTRO DE VICTORIAS
elif menu == "✨ Registro de Victorias":
    st.subheader("✨ Tu Libro de Victorias")
    st.write("Cada pequeño hechizo completado cuenta. Anota tu logro de hoy:")
    
    victoria = st.text_input("¿Qué victoria lograste hoy?")
    if st.button("Guardar en el Libro"):
        if victoria:
            if 'victorias' not in st.session_state:
                st.session_state.victorias = []
            st.session_state.victorias.append(victoria)
            st.success("¡Registrado en las estrellas! Eres increíble. 💖")
    
    if 'victorias' in st.session_state and st.session_state.victorias:
        st.write("### Tus logros recientes:")
        for v in st.session_state.victorias:
            st.markdown(f"- ✨ {v}")

st.markdown(f"""
    <div class="firma">
        Hecho con magia y amor para ti y Okami 🌸🐾
    </div>
""", unsafe_allow_html=True)