#!/usr/bin/python3


def get_page(name, filepath):
  pages_dict = {
      'index': page_index,
      'account-data': page_account_data,
      'movie-ratings': page_movie_ratings,
      'list': page_list,
      'lists': page_lists,
      'friend-group': page_friend_group,
      'friend-groups': page_friend_groups
  }  

  page_reader = pages_dict[name]

  return page_reader.get_data(load_html(filepath))