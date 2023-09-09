const request = new Request("http://127.0.0.1:5000");
const getArticlesUrl = 'http://127.0.0.1:5000/get_articles';
const addArticleUrl = 'http://127.0.0.1:5000/add_article';
const deleteArticleUrl = 'http://127.0.0.1:5000/node/article/';

$(document).ready(function () {
    // Charger les articles existants lors du chargement de la page
    loadArticles();

    // Soumission du formulaire pour ajouter un nouvel article
    $('#add-article-form').submit(function (e) {
        e.preventDefault();
        var title = $('#title').val();
        var content = $('#content').val();

        if (title && content) {
            addArticle(title, content);
        }
    });

    // Fonction pour charger les articles existants
    function loadArticles() {
        fetch(getArticlesUrl)
            .then((response) => {
                if (response.status === 200) {
                    return response.json();
                } else {
                    throw new Error("Something went wrong on API server!");
                }
            })
            .then((response) => {
                // Effacer la liste actuelle d'articles
                $('#article-list').empty();

                // Parcourir les articles et les ajouter à la liste
                response.data.forEach(function (article) {
                    var listItem = $('<li>');
                    var articleId = article.id;

                    // Créez un bouton de suppression avec l'attribut data-article-id
                    var deleteButton = $('<button>');
                    deleteButton.addClass('delete-article');
                    deleteButton.attr('data-id', articleId);
                    deleteButton.text('Supprimer');

                    // Ajoutez le bouton à l'élément de liste
                    listItem.html(article.attributes.title + ' ');
                    listItem.append(deleteButton);

                    $('#article-list').append(listItem);
                });

                // Gérer la suppression d'un article
                $('.delete-article').click(function () {
                    var articleId = $(this).data('id');
                    deleteArticle(articleId);
                });
            })
            .catch((error) => {
                console.error(error);
            });
    }

    // Fonction pour ajouter un nouvel article
    function addArticle(title, content) {
        var jsonData = {
            title: title,
            content: content
        };

        fetch(addArticleUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(jsonData)
        })
            .then((response) => {
                if (response.status === 201) {
                    return response.json();
                } else {
                    throw new Error("Something went wrong on API server!");
                }
            })
            .then((data) => {
                loadArticles();
                $('#title').val('');
                $('#content').val('');
            })
            .catch((error) => {
                console.error(error);
            });
    }

    // Fonction pour supprimer un article
    function deleteArticle(articleDrupalId) {
        console.log("Suppression de l'article avec l'ID de Drupal : " + articleDrupalId); // Affiche un message de débogage avec l'ID de Drupal
        
        const request = new Request(deleteArticleUrl + articleDrupalId);
        console.log("URL de suppression de l'article : " + request.url); // Affiche l'URL complète de suppression de l'article
        
        fetch(request, {
            method: 'DELETE'
        })
        .then((response) => {
            if (response.status === 204) {
                console.log("Suppression réussie !");
                loadArticles(); // Rechargez la liste des articles après la suppression
            } else {
                console.error("Erreur lors de la suppression de l'article : " + response.status);
                throw new Error("Something went wrong on API server!");
            }
        })
        .catch((error) => {
            console.error(error);
        });
    }
    
});
