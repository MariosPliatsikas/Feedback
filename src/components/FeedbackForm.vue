<template>
  <div>
    <h2>Feedback Form</h2>
    <form @submit.prevent="submitFeedback">
      <label>
        Feedback:
        <textarea v-model="feedback" required></textarea>
      </label>
      <button type="submit">Submit Feedback</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      feedback: '',
    };
  },
  methods: {
    async submitFeedback() {
      try {
        await axios.post('http://localhost:5000/feedback', { feedback: this.feedback });
        this.feedback = '';
        alert('Feedback submitted successfully!');
      } catch (error) {
        console.error(error);
        alert('Failed to submit feedback');
      }
    },
  },
};
</script>
