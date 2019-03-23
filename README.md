# post-forum-by-xander
Full-stack Django - CRUD app for posting

Routes/Actions

    /categories: A list of all the categories
    /categories/new: The form for a new category
    /categories/:id: See a specific category and a list of all of its associated posts
    /categories/:id/edit: Edit page for a specific category
    Also, the ability to update/destroy categories
    /categories/:category_id/posts/new: The form for a new post under a specific category
    /categories/:category_id/posts/:post_id: See a specific post for a specific category, have the ability go back to all of    the post's category's other posts (/categories/:category_id/posts)
    /categories/:category_id/posts/:post_id/edit: Edit page for a specific post under a specific category
    Also, the ability to update/destroy posts

