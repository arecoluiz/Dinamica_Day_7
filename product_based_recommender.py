import random

import numpy as np

from data import get_data, get_product_based_similarity_matrix


class ProductBasedRecommender:

  def __init__(self, data_path):
    self.data_path = data_path

  def setup(self):
    data = get_data(self.data_path)
    sim_matrix, available_products_index = get_product_based_similarity_matrix(data)
    self.available_products_index = available_products_index
    self.sim_matrix = sim_matrix

  def get_random_product_index(self):
    product_id = self.available_products_index[random.randint(0, self.sim_matrix.shape[0])]
    return product_id

  def get_n_closest(self, product_id, n=10):
    if product_id not in self.available_products_index:
      raise ValueError('Product is not available on data.')
    product_index = self.available_products_index.tolist().index(product_id)
    closest_n_products = np.argsort(-self.sim_matrix[product_index])[1:n]
    n_closest = []
    for product_data in zip(self.available_products_index[closest_n_products], self.sim_matrix[product_index][closest_n_products]):
      n_closest.append(product_data)
    return tuple(n_closest)
