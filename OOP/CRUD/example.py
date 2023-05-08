# class Post:
#     id = 0

#     def __init__(self, user) -> None:
#         self.user = user
#         self.posts = []

#     # CRUD
#     def create_post(self, title, body, image):
#         Post.id += 1
#         post = dict(id=self.id, title=title, body=body, image=image)
#         self.posts.append(post)
#         return {'status': 201, 'msg': 'successfully created'}
    
#     def retrieve_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 return {'status': 200, 'content': post}
#         return {'status': 404, 'msg': 'Not found!'}
    
#     def update_post(self, post_id, **kwargs):
#         for post in self.posts:
#             if post['id'] == post_id:
#                 index = self.posts.index(post)
#                 self.posts[index].update(**kwargs)
#                 return {'status': 200, 'msg': 'updated'}
#         return {'status': 404, 'msg': 'Not found!'}
    
#     def delete_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 self.posts.remove(post)
#                 return {'status': 204, 'msg': 'No content!'}
#         return {'status': 404, 'msg': 'Not found!'}

# acc1 = Post('JohnSnow')
# acc2 = Post('JamieLanister')

# acc1.create_post('Good News', 'Sansa rodila dochku!!', 'http://localhost:8000/images/foto.jpg')
# acc1.create_post('Na progulke!', 'na chile', 'http://foto.jpg')
# acc1.create_post('Egipet!!', 'Lechu v Egipet', 'http://goto123.jpg')

# acc2.create_post('Jamie', 'Post Jamie', 'https://jamie.jpg')

# acc1.create_post('Turkey!!', 'Lechu v Turkey', 'http://goto123.jpg')

# print(acc1.user)
# print(acc1.posts)
# print(acc2.posts)

# print(acc1.retrieve_post(1))
# print(acc1.retrieve_post(5))

# print(acc1.update_post(1, title='Suyunchu!!'))

# print(acc1.retrieve_post(1))
# print(acc1.delete_post(1))

# print(acc1.posts)
# print(acc2.posts)