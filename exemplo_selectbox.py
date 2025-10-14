import streamlit as st
st.sidebar.image("logoplay")

# Dados de exemplo
generos = ["Rock", "Trap", "POP"]

# Dicionário relacionando gêneros aos seus livros
artista_por_genero = {
    "Rock": ["Nickelback", "Daftones"],
    "Trap": ["Travis Scott", "Drake", "Don Toliver"],
    "POP": ["Laufey", "Addison Rae", "Taylor Swift"]
}

# Selectbox para escolher o gênero                
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    artista_selecionado = st.sidebar.selectbox(
        "Selecione o artista:", 
        artista_por_genero[genero_selecionado]
        )

# Mostrar apenas o livro selecionado
if genero_selecionado and artista_por_genero:
    st.write(f"**Artista selecionado:** {artista_selecionado}")
    st.write(f"**Gênero:** {genero_selecionado}")

# Mostrar video
if genero_selecionado == "Rock" and artista_por_genero == "Nickelback":
    st.video("https://youtu.be/Aiay8I5IPB8?si=VQGAjAr1ryG2LdPE")

elif genero_selecionado == "Rock" and artista_por_genero == "Daftones":
    st.video("https://youtu.be/ifN91YvHj7g?si=BLhOAoo_liY-jI_J")

elif genero_selecionado == "Trap" and artista_por_genero == "Travis Scott":
    st.video("https://youtu.be/B9synWjqBn8?si=e5aBY8AWShu4QFDA")

elif genero_selecionado == "Trap" and artista_por_genero == "Drake":
    st.video("https://youtu.be/JFm7YDVlqnI?si=FQcJLiBNwEjgMs4q")

elif genero_selecionado == "Trap" and artista_por_genero == "Don Toliver":
    st.video("https://youtu.be/_r-nPqWGG6c?si=pkr75PzCawlN-yNh")

elif genero_selecionado == "POP" and artista_por_genero == "Laufey":
    st.video("https://youtu.be/Yq6qkq_TWAM?si=mpn11AGHyitON_Ac")

elif genero_selecionado == "POP" and artista_por_genero == "Addison Rae":
    st.video("https://youtu.be/beNFK2cdnKU?si=4FWzqcu1mugjmGlY")

elif genero_selecionado == "POP" and artista_por_genero == "Taylor Swift":
    st.video("https://youtu.be/pB-MmaoO6B8?si=QddocAi_LWgzueAS")







