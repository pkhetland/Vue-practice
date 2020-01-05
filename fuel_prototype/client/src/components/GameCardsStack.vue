<template>
  <div class="col-12 gamecardcol h-100">
    <GameCard
      v-for="(card, index) in cards"
      :key="card"
      :card="card"
      :is-current="index === 0"
      @cardAccepted="$emit('cardAccepted');"
      @cardRejected="$emit('cardRejected');"
      @cardSkipped="$emit('cardSkipped');"
      @hideCard="$emit('hideCard');"
      />
  </div>
</template>

<script>
import GameCard from './GameCard.vue'

export default {
  components: {
    GameCard
  },

  props: {
    cards: {
      type: Array,
      required: true
    }
  }

}
</script>

<style lang="scss" scoped>

.gamecardcol {
  padding: 0;
  align-content: center;
  justify-content: center;
  max-height: 80vh;
}
</style>
