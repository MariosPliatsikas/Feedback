<!-- FeedbackForm.vue -->
<template>
  <div>
    <h2>Feedback Form</h2>
    <form @submit.prevent="submitFeedback">
      <label>   
        Feedback Type:
        <select v-model="feedbackType">
          <option value="positive">Positive</option>
          <option value="negative">Negative</option>
        </select>
      </label>
      <label>
        Comments:
        <textarea v-model="comments"></textarea>
      </label>
      <button type="submit">Submit Feedback</button>
    </form>
  </div>
</template>

<script>
export default {  
  data() {
    return {
      feedbackType: 'positive',
      comments: '',
    };
  },
  methods: {
    submitFeedback() {
      // Send feedback data to the backend (to be implemented later)
      console.log('Feedback submitted:', this.feedbackType, this.comments);
    },
  },
};
</script>

<style scoped>
/* Your component styles go here */

/* Example styles: Feel free to customize as needed */
h2 {
  color: #333;
  font-size: 24px;
  margin-bottom: 20px;
}

</style>
