# from django.urls import reverse_lazy
# from django.views.generic.edit import DeleteView, UpdateView
# from apps.comment.models import Comment

# class CommentDeleteView(DeleteView):
#     model = Comment
#     template_name = 'comment/delete.html'  # You need to create this template
#     context_object_name = 'comment'

#     def get_success_url(self):
#         return reverse_lazy('detail', kwargs={'pk': self.object.news.id})


# class CommentUpdateView(UpdateView):
#     model = Comment
#     fields = ['text']
#     template_name = 'comment/update.html'
#     context_object_name = 'comment'

#     def get_success_url(self):
#         return reverse_lazy('detail', kwargs={'pk': self.object.news.id})