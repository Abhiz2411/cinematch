import base64

def encode_to_base64(input_path, output_path):
    with open(input_path, 'rb') as f:
        encoded = base64.b64encode(f.read())
    with open(output_path, 'wb') as f:
        f.write(encoded)

# Encode both pickle files
encode_to_base64('model/movie_list.pkl', 'model/movie_list.pkl.b64')
encode_to_base64('model/similarity.pkl', 'model/similarity.pkl.b64')
