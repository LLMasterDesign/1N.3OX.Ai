import { StarIcon } from '@heroicons/react/20/solid'

const testimonials = [
  {
    body: 'This platform transformed how we approach AI prompts. Our content generation improved by 40% and we cut costs by 30%. The research-backed techniques actually work.',
    author: {
      name: 'Sarah Chen',
      handle: 'sarahchen',
      role: 'Content Director',
      company: 'TechFlow',
      imageUrl: 'https://images.unsplash.com/photo-1494790108755-2616b612b786?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=100&q=80',
    },
  },
  {
    body: 'As a consultant, I needed to optimize prompts for different clients. This platform gave me the tools and insights to deliver consistent, high-quality results every time.',
    author: {
      name: 'Marcus Rodriguez',
      handle: 'marcusr',
      role: 'AI Consultant',
      company: 'InnovateAI',
      imageUrl: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=100&q=80',
    },
  },
  {
    body: 'The A/B testing feature alone paid for itself in the first month. We discovered that small changes to our prompts had massive impacts on output quality.',
    author: {
      name: 'Emily Watson',
      handle: 'emilyw',
      role: 'Product Manager',
      company: 'DataDriven Inc',
      imageUrl: 'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=100&q=80',
    },
  },
]

export function Testimonials() {
  return (
    <div className="bg-gray-50 py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-xl text-center">
          <h2 className="text-lg font-semibold leading-8 tracking-tight text-primary-600">Testimonials</h2>
          <p className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Loved by teams worldwide
          </p>
        </div>
        <div className="mx-auto mt-16 flow-root max-w-2xl sm:mt-20 lg:mx-0 lg:max-w-none">
          <div className="-mt-8 sm:-mx-4 sm:columns-2 sm:text-[0] lg:columns-3">
            {testimonials.map((testimonial, testimonialIdx) => (
              <div key={testimonialIdx} className="pt-8 sm:inline-block sm:w-full sm:px-4">
                <figure className="rounded-2xl bg-white p-8 text-sm leading-6 shadow-sm ring-1 ring-gray-900/5">
                  <blockquote className="text-gray-900">
                    <p>"{testimonial.body}"</p>
                  </blockquote>
                  <figcaption className="mt-6 flex items-center gap-x-4">
                    <img
                      className="h-10 w-10 rounded-full bg-gray-50"
                      src={testimonial.author.imageUrl}
                      alt=""
                    />
                    <div>
                      <div className="font-semibold text-gray-900">{testimonial.author.name}</div>
                      <div className="text-gray-600">
                        {testimonial.author.role} at {testimonial.author.company}
                      </div>
                    </div>
                  </figcaption>
                </figure>
              </div>
            ))}
          </div>
        </div>
        <div className="mt-16 text-center">
          <div className="flex items-center justify-center gap-x-1">
            {[0, 1, 2, 3, 4].map((rating) => (
              <StarIcon key={rating} className="h-5 w-5 flex-none text-yellow-400" aria-hidden="true" />
            ))}
          </div>
          <p className="mt-2 text-sm text-gray-600">
            <span className="font-semibold">4.9/5</span> average rating from 500+ users
          </p>
        </div>
      </div>
    </div>
  )
}