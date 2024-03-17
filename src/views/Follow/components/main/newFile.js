import { ref } from 'vue';

export default (await import('vue')).defineComponent({
name: 'FollowedList',
setup() {
const selectedButton = ref('Latest');
const selectButton = (button) => {
selectedButton.value = button;
}, data; () => {
return {
// This would be fetched from an API or a store in a real app
followedPeople: [
{ id: 1, name: 'Bob Sponge', description: 'MSc Computing Science. I am a Master student in computing science and I love diving.', avatar: 'path_to_avatar.jpg' },
{ id: 2, name: 'Le Siway', description: 'MSc Computing Science. I am a Master student in computing science and I love diving.', avatar: 'path_to_avatar.jpg' },
// ... more people
]
};
},
methods; {
unfollow(personId); {
// Here you would call an API to unfollow the person
console.log(`Unfollow person with id: ${personId}`);
this.followedPeople = this.followedPeople.filter(person => person.id !== personId);
}
}
}
});
