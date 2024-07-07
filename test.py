from src.utils.gpt_created_data_provider import GPT_Created_Data_Provider

new_set = GPT_Created_Data_Provider().provide_data_as_numpy_array()
print(new_set.shape)