<template>
  <b-row class='w-100 h-25 justify-content-around'>
    <b-col class='icon icon2 col-3'>
      <thumbs-down-icon
      size="2x"
      color="#E56565"
      class=""
      @click="$emit('decreaseRating')"
      />
    </b-col>
    <b-col class='icon icon2 col-3'>
      <!-- <star-icon
      size="2x"
      color="gold"
      class=""
      @click="$emit('triggerStarCard');"/> -->
    </b-col>
    <b-col class='icon icon2 col-3'>
      <thumbs-up-icon
      size="2x"
      color="#4BB182"
      class=""
      @click="$emit('increaseRating')"
      />
    </b-col>
  </b-row>
</template>

<script>
import { ThumbsUpIcon, ThumbsDownIcon } from 'vue-feather-icons'
export default {
  data () {
    return {
      thumbsUpDeactive: false,
      thumbsDownDeactive: false
    }
  },
  components: {
    /* StarIcon, */
    ThumbsUpIcon,
    ThumbsDownIcon
  },
  methods: {
    hideCard () {
      this.$emit('hideCard', this.$parent.visibleCards[0])
    }
  }
}
</script>

<style scoped>
.footer {
  color: whitesmoke;
  }

svg {
  display: inline-block;
}

.test {
  color: white;
}

</style>
