import numpy as np
import gensim


def get_word2vec_embedding(word, model, dimensions):
    vec_rep = np.random.rand(dimensions)
    if word in model:
        vec_rep = model[word]

    return vec_rep


def add_word_vectors_to_embeddings(word_index, word_vector_path, encoder_embedding_matrix, decoder_embedding_matrix,
                                   vocab_size, embedding_size):

    wv_model_path = word_vector_path + "GoogleNews-vectors-negative300.bin.gz"
    wv_model = gensim.models.KeyedVectors.load_word2vec_format(
        wv_model_path, binary=True, unicode_errors='ignore')

    i = 0
    for key in word_index:
        word_embedding = get_word2vec_embedding(key, wv_model, embedding_size)
        encoder_embedding_matrix[i] = word_embedding
        decoder_embedding_matrix[i] = word_embedding 
        i += 1
        if i >= vocab_size:
            break

    del wv_model

    return encoder_embedding_matrix, decoder_embedding_matrix
