import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def get_data(path):
  return pd.read_csv(path)


def start_pipeline(dataf):
  return dataf.copy()


def get_product_count(dataf):
  return dataf.groupby(by='product_id', as_index=False) \
    .agg({'order_id': pd.Series.nunique}) \
    .rename(columns={'order_id': 'order_id_count'}) \
    .set_index('product_id') \
    .sort_values('order_id_count', ascending = False)


def get_n_top_values(dataf, n):
  return dataf.head(n) \
    .index \
    .tolist()


def format_sample(dataf):
  return pd.DataFrame({
      "pedidos": dataf["order_id"],
      "produto": dataf["product_id"],
      "action": dataf["review_score"]
  })


def get_top_products_ids(dataf, sample_size=1000):
  return dataf \
    .pipe(start_pipeline) \
    .pipe(get_product_count) \
    .pipe(get_n_top_values, sample_size)


def get_product_based_similarity_matrix(data):
  top_product_ids = get_top_products_ids(data)
  product_sampled_relationship_data = data[data["product_id"].isin(top_product_ids)] \
    .pipe(format_sample) \
    .pivot_table(index="pedidos", columns="produto", values="action").fillna(0)
  return cosine_similarity(product_sampled_relationship_data.T), product_sampled_relationship_data.T.index
