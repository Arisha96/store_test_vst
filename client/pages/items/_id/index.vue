<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ item.name }}</h2>
      </div>
      <div class="col-md-6 mb-4">
        <img
          class="img-fluid"
          style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
          :src="item.image.content"
          alt
        >
      </div>
      <div class="col-md-6">
        <div class="item-details">
          <h4>{{ item.name }}</h4>
          <h5><b>Cost:</b> {{ item.cost }} {{ item.cost_type }}</h5>
          <b-tabs content-class="mt-3">
          <b-tab title="Description" active><p>{{ item.description }}</p></b-tab>
          <b-tab title="Properties">
          <template v-for="prop in item.properties">
            <p><b>{{ prop.name }}:</b> {{ prop.description }}</p>
          </template>
          </b-tab>
          </b-tabs>
          <div class="action-buttons">
            <nuxt-link :to="`/items`" class="btn btn-sm btn-success">Back to the list</nuxt-link>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head() {
    return {
      title: "View Item"
    };
  },
  async asyncData({ $axios, params }) {
      let item = await $axios.$get(`/items/${params.id}`);
      console.log(item);
      let props = await $axios.$get(`/items/${params.id}/properties`);
      item["properties"] = props["results"];
      console.log(item);
      return { item };
  },
  data() {
    return {
      recipe: {
        name: "",
        image: "",
        properties: "",
        cost: "",
        cost_type: "",
        description: null,
      }
    };
  }
};
</script>
<style scoped>
</style>
