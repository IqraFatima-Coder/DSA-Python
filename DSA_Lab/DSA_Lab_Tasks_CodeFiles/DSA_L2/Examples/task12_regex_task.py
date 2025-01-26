import re 
text = "The rain in Spain falls mainly in the plain." 
# Find all words starting with 'S' 
pattern = r"\bS\w+" 
result = re.findall(pattern, text) 
print("Words starting with S:", result) 
# Replace 'rain' with 'snow' 
modified_text = re.sub(r"rain", "snow", text) 
print("Modified text:", modified_text) 