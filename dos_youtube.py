from apiclient.discovery import build
from Youtube import Video
from Youtube import AbstractYoutube

class AppYoutube(AbstractYoutube):
    def InfoVideo(self, url):

        API_KEY = 'AIzaSyBOcBaTZx4cZdVvrVdQujN4TuoC9vP0F8A'
        youtube = build('youtube', 'v3', developerKey=API_KEY)

        ids = url[32:43]
        results = youtube.videos().list(id=ids, part='snippet').execute()
        for result in results.get('items', []):
            NombreCanal = (result['snippet']['channelTitle'])
            Titulo = (result['snippet']['title'])
            Descripcion = (result['snippet']['description'])
            Publicacion = result['snippet']['publishedAt']

        results1 = youtube.videos().list(id=ids, part='statistics').execute()
        for result2 in results1.get('items', []):
            Likes = result2['statistics']['likeCount']
            Vistas = result2['statistics']['viewCount']

        results4 = youtube.videos().list(id=ids, part='contentDetails').execute()
        for result5 in results4.get('items', []):
            Duracion = result5['contentDetails']['duration']

        return Video(Titulo, Duracion, NombreCanal, Publicacion, Likes, Vistas, Descripcion)

if __name__ == '__main__':
    y = AppYoutube()
    vid = y.InfoVideo('https://www.youtube.com/watch?v=7I7u_XLtFa0')

    print(vid.Descripcion)
    print(vid.Nombre)
    print(vid.Canal)
    print(vid.Duracion)
    print(vid.Fecha)
