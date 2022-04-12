<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>Magic Stuff</h3>
        </div>
      </div>
      <template v-for="item in items">
        <div :key="item.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <item-card :item="item"></item-card>
        </div>
      </template>
    </div>
  </main>
</template>

<script>
import ItemCard from "~/components/ItemCard.vue";

export default {
  head() {
    return {
      title: "Magic Stuff"
    };
  },
  components: {
    ItemCard
  },
  async asyncData({ $axios, params }) {
    try {
      let items = await $axios.$get('/items/');
      items = items['results'];
      console.log(items);
      return { items };
    } catch (e) {
      return { items: [] };
    }
  },
  data() {
    return {
      items: []
    };
  },
};
</script>
<style scoped>
</style>
