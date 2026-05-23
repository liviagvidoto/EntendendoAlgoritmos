# OCR (Optical Character Recognition) é o processo de converter imagens de texto em texto editável. 
# Ele é amplamente utilizado para digitalizar documentos, reconhecer placas de veículos, processar cheques bancários e muito mais. 
# O OCR envolve várias etapas, incluindo pré-processamento da imagem, segmentação de caracteres, reconhecimento de caracteres e pós-processamento para melhorar a precisão.

def ocr(img):
    # Pré-processamento da imagem
    img = preprocessamentoImg(img)

    # Segmentação de caracteres
    caracteres = segmentarCaracteres(img)

    # Reconhecimento de caracteres
    textoReconecido = ""
    for caractere in caracteres:
        textoReconecido += reconhecerCaractere(caractere)

    # Pós-processamento para melhorar a precisão
    textoFinal = posProcessarTexto(textoReconecido)

    return textoFinal