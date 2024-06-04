from langserve import RemoteRunnable

chat_model = RemoteRunnable("http://localhost:8080/chat")

print(f"Pinging chat model: {chat_model.invoke('help').content}")

instruct_model = RemoteRunnable("http://localhost:8080")
print(f"Pinging instruct model: {instruct_model.invoke('help')}")
