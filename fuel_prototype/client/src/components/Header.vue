<template>
  <b-container class='header'>
    <b-row class="justify-content-start">
      <b-col>
        <a href=''><ArrowLeftIcon class="mt-1 ml-2"/></a>
      </b-col>
      <b-col class="col-12">
        <p>{{ headerText }}</p>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import { ArrowLeftIcon } from 'vue-feather-icons'

export default {
  components: {
    ArrowLeftIcon
  },
  props: {
    headerText: {
      type: Object,
      default: function () {
        return ''
      }
    }
  }
}
</script>

<style lang="scss" scoped>

a {
  color: white;
}

ArrowLeftIcon {
  position: relative;
}

headerText {
  text-align: left;
}

.header {
  margin-bottom: 3vh;
  margin-top: 3vh;
  color: whitesmoke;
}

.text-row {
  top: 0;
}

.roundCounter {
  font-size: 1rem;
}
</style>
