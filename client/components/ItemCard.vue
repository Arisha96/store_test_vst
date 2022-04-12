<template>
  <div class="card item-card">
    <img :src="item.image.content" class="card-img-top" >
    <div class="card-body">
      <h5 class="card-title">{{ item.name }}</h5>
      <p class="card-text">
        <p><strong>Cost:</strong> {{ item.cost }} {{ item.cost_type }}</p>
      </p>
      <div class="action-buttons">
        <nuxt-link :to="`/items/${item.id}/`" class="btn btn-sm btn-success">View</nuxt-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
    props: ["item"]
};
</script>
<style>
.recipe-card {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
}
</style>
