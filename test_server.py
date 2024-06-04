from langserve import RemoteRunnable

chat_model = RemoteRunnable("http://localhost:8080/chat")

print(chat_model.invoke("help"))

instruct_model = RemoteRunnable("http://localhost:8080")
print(instruct_model.invoke("help")
