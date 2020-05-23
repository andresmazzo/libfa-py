
import libfa.web.v1.pages.page_index, libfa.web.v1.pages.page_movie_info

def get_page(name, filepath):
  dicts = {
      'index': page_index,
      'movie-info': page_movie_info
  }  

  page = dicts[name]

  return page.get(filepath)

