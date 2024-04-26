import requests
from wordcloud import WordCloud


def main():
    contenido_web = requests.get("https://danielmaldonado.com.ar/linux.txt")
    wc = WordCloud(min_word_length=5).process_text(contenido_web.text)
    
    for palabra in wc:
        print(palabra)
    
    

if __name__ == "__main__":
    main()
