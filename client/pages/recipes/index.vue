<template>
    <main class="container mt-5">
      <div class="row">
        <div class="col-12 text-right mb-4">
          <div class="d-flex justify-content-between">
            <h3>La Recipes</h3>
            <nuxt-link to="/recipes/add" class="btn btn-info">Add Recipe</nuxt-link>
          </div>
        </div>
        <div v-for="recipe in recipes" :key="recipe.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <recipe-card :onDelete="deleteRecipe" :recipe="recipe"></recipe-card>
        </div>
      </div>
    </main>
  </template>
  
  <script>
  import RecipeCard from "~/components/RecipeCard.vue";
  
  export default {
    head() {
      return {
        title: "Recipes list"
      };
    },
    components: {
      RecipeCard
    },
    async asyncData({ $axios }) {
      try {
        const recipes = await $axios.$get('/recipes/');
        return { recipes };
      } catch (e) {
        console.error('Error fetching recipes:', e);
        return { recipes: [] };
      }
    },
    data() {
      return {
        recipes: []
      };
    },
    methods: {
      async deleteRecipe(recipe_id) {
        try {
          await this.$axios.$delete(`/recipes/${recipe_id}/`);
          const newRecipes = await this.$axios.$get('/recipes/');
          this.recipes = newRecipes;
        } catch (e) {
          console.error('Error deleting recipe:', e);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  </style>
  