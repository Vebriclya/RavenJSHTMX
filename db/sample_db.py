from random import randint

db = {
    "posts": [
        {
            "id": 1,
            "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. ",
            "content": "Nam ultrices lobortis nulla, dictum tincidunt lectus iaculis et. Donec a felis risus. Mauris eu egestas nulla. Quisque nec viverra erat. Duis a felis non tortor viverra tempus. Suspendisse malesuada tellus ut libero egestas porttitor. Proin lectus mauris, finibus fermentum nunc a, sodales vehicula felis. Sed bibendum quam erat, ac vestibulum orci accumsan at. Praesent maximus eros velit, ac cursus elit sodales non. Morbi ut tincidunt urna. Vestibulum auctor, eros sit amet pellentesque molestie, lacus arcu ullamcorper nisl, eu auctor sapien nisi et tellus. Praesent pulvinar dui non mollis suscipit. Cras dignissim justo sed justo pellentesque, molestie scelerisque felis varius. ",
        },
        {
            "id": 2,
            "title": "Aenean pellentesque aliquet ipsum, et.",
            "content": " Nam non euismod orci. Donec in semper lorem, aliquam feugiat nunc. In rutrum magna sed tortor dapibus, eget lacinia libero ultricies. Morbi volutpat massa at sagittis dapibus. Pellentesque porta sed nibh et volutpat. Donec arcu sapien, lacinia sed fringilla nec, porttitor eu ipsum. In in lectus finibus, sodales ligula et, convallis risus. Integer sem urna, auctor at turpis feugiat, tristique sollicitudin urna. Vivamus ut sem hendrerit, porttitor urna at, dignissim tortor. Pellentesque eleifend finibus arcu nec ornare. Nunc in justo consequat, porttitor sapien ut, ultricies velit. Curabitur euismod mauris orci, at laoreet erat dictum vel. Suspendisse quis risus quis tellus euismod facilisis. Vivamus non erat in augue blandit ullamcorper eu ut sem. Nullam sed justo eu magna tristique dapibus et quis leo. In tristique eu purus eu lobortis. Nullam ac quam ultrices, rhoncus nibh sed, tincidunt ante. Sed efficitur feugiat fermentum. Donec aliquet iaculis libero eu aliquet. Nulla facilisi. Sed rhoncus posuere metus, eu semper velit varius ac. Nam quis neque ac eros egestas fermentum. Pellentesque id nisl vel lacus lacinia vestibulum. Mauris at posuere ligula. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla rhoncus, lectus vitae consectetur sagittis, nisl magna tempus lorem, id ultricies nulla orci id odio. Pellentesque finibus commodo tortor at posuere. Sed dignissim tempus auctor. Etiam leo odio, ultricies quis orci vitae, pharetra bibendum diam.",
        },
        {
            "id": 3,
            "title": "Phasellus pharetra, lectus et scelerisque semper. ",
            "content": "Duis vel semper tellus. Mauris id lectus vitae metus aliquam tristique. Integer tincidunt lacinia libero id laoreet. Donec pellentesque leo vitae eros molestie congue. Morbi fermentum, turpis vitae tristique varius, lectus sapien lacinia turpis, a tempus urna lorem non dolor. Sed porta arcu et malesuada sagittis. Proin dui dui, lacinia ac congue at, pulvinar et tellus. Vestibulum consectetur purus lorem, sagittis pharetra dolor blandit et. Morbi ac dolor non odio placerat ultricies. Proin vel volutpat urna. Phasellus suscipit maximus quam id pretium. Nam suscipit, erat non facilisis faucibus, augue ligula placerat nisi, id elementum nisi libero in purus. Mauris eros massa, aliquet sed purus et, egestas egestas dui. ",
        },
    ]
}


def get_posts():
    global db
    return db["posts"]


def get_post(post_id):
    global db
    for post in db["posts"]:
        if post["id"] == post_id:
            return post
    return None


def add_post(title, content):
    global db
    post = {
        "id": randint(1000, 9999),
        "title": title,
        "content": content,
    }
    db["posts"].insert(0, post)
    return post


def update_post(id, title, content):
    global db
    for post in db["posts"]:
        if post["id"] == id:
            post["title"] = title
            post["content"] = content
            return post
    return None


def delete_post(id):
    global db
    db["posts"] = [post for post in db["posts"] if post["id"] != id]
