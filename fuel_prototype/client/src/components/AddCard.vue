
<template>
  <b-container id="addCard">
    <b-row class="align-content-center justify-center h-100">
      <b-col class="col-12">
        <alert :message="message" v-if="showMessage"/>
      </b-col>
      <b-col class="col-12">
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group id="form-title-group"
          label="Title:"
          label-for="form-title-input">
            <b-form-input id="form-title-input"
            type="text"
            v-model="addCardForm.title"
            required
            placeholder="Enter title">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-category-group"
          label="Category:"
          label-for="form-category-input">
            <b-form-input id="form-author-input"
            type="text"
            v-model="addCardForm.category"
            required
            placeholder="Enter category">
            </b-form-input>
          </b-form-group>
          <b-form-group id="form-text-group"
          label="Card text:"
          label-for="form-text-input">
            <b-form-input id="form-text-input"
              type="text"
              v-model="addCardForm.text"
              required
              placeholder="Enter text">
            </b-form-input>
          </b-form-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>

import axios from 'axios'
import Alert from './Alert.vue'

export default {
  data () {
    return {
      addCardForm: {
        title: '',
        category: '',
        text: ''
      },
      path: 'http://localhost:5000/cards',
      visibleCards: [],
      message: '',
      showMessage: false
    }
  },
  components: {
    alert: Alert
  },
  methods: {
    getCards () {
      axios.get(this.path)
        .then((res) => {
          this.visibleCards = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    },
    addCard (payload) {
      axios.post(this.path, payload)
        .then(() => {
          this.getCards()
          this.message = 'Book added!'
          this.showMessage = true
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getCards()
        })
    },
    initForm () {
      this.addCardForm.title = ''
      this.addCardForm.category = ''
      this.addCardForm.text = ''
    },
    onSubmit (evt) {
      evt.preventDefault()
      const payload = {
        function: 'add',
        title: this.addCardForm.title,
        category: this.addCardForm.category,
        text: this.addCardForm.text
      }
      this.addCard(payload)
      this.initForm()
    },
    onReset (evt) {
      evt.preventDefault()
      this.initForm()
      this.showMessage = false
    }
  },
  created () {
    this.getCards()
  }
}
</script>

<style lang="scss">

#form-title-group, #form-category-group, #form-text-group {
  color: white;
}

#form-category-group, #form-text-group {
  color: white;
  margin-top: 50px;
}

#addCard {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  text-align: center;
  height: 720px;
  width: 375px;
  background-size: cover;
  background-image: linear-gradient(#190048, #0e0027);
  overflow: hidden;
  padding: 0;
  border: solid 7px;
  border-color: black;
  border-radius: 20px;
  // box-shadow: 10px black;
}

.red {
  background-size: cover;
  background-image: linear-gradient( #CB2854, #CB4D2F);
}

.orange {
  background-size: cover;
  background-image: linear-gradient( #D38312, #f5af19);
}

.blue {
  background-size: cover;
  background-image: linear-gradient( #4b6cb7, #49a09d);
}

</style>
