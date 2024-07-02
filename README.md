Create a simple blog application where users can register, create and edit posts.
 
**Models**

1) User.
Use Django's built-in User model with an extension for additional field.
Bio: TextField
2) Post.
Title: CharField
Content: TextField
Author: ForeignKey to User
Created_at: DateTimeField(auto_now_add=True)
Updated_at: DateTimeField(auto_now=True)
 
**Views**

1) Home Page: List of all posts with pagination.
2) Post Detail: Detailed view of a single post with its comments.
3) Create Post: Form for creating a new post (login required).
4) Edit Post: Form for editing an existing post (login required, author only).
5) Delete Post: Option to delete a post (login required, author only).
 
**Templates**

1) Base Template: Base HTML template with navigation bar (home, login, register, etc.).
2) Home Template: Template displaying the list of posts.
3) Post Detail Template: Template displaying the post details and comments.
4) Post Form Template: Template for creating and editing a post.
 
**Forms**

1) User Registration Form: Form for user registration.
2) User Login Form: Form for user login.
3) Post Form: Form for creating and editing a post.
 
**Authentication**

Use Django’s built-in authentication system for user registration and login.
Ensure that only authenticated users can create, edit and delete posts.
Ensure that only the author of a post can edit or delete it.
 
**Tips**

For user registration and login I would suggest overriding generic Django views.
1) https://docs.djangoproject.com/en/5.0/topics/auth/default/ - docs about that.
2) https://www.youtube.com/watch?v=3aVqWaLjqS4
3) https://www.youtube.com/watch?v=q4jPR-M0TAQ - good videos on the topic of registration.