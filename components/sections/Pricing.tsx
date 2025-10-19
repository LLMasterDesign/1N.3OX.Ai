import { CheckIcon } from '@heroicons/react/20/solid'
import { Button } from '@/components/ui/Button'

const tiers = [
  {
    name: 'Starter',
    id: 'tier-starter',
    href: '/signup?plan=starter',
    priceMonthly: 'Free',
    priceYearly: 'Free',
    description: 'Perfect for individuals and small projects getting started with prompt optimization.',
    features: [
      '10 prompt optimizations per month',
      'Basic analytics dashboard',
      'Access to technique library',
      'Community support',
      'Standard optimization algorithms',
      'Email support',
    ],
    mostPopular: false,
  },
  {
    name: 'Professional',
    id: 'tier-professional',
    href: '/signup?plan=professional',
    priceMonthly: '$29',
    priceYearly: '$290',
    description: 'Ideal for content creators, consultants, and small businesses scaling their AI usage.',
    features: [
      'Unlimited prompt optimizations',
      'Advanced analytics and reporting',
      'A/B testing capabilities',
      'Priority support',
      'Advanced optimization techniques',
      'Export/import functionality',
      'Team collaboration (up to 5 users)',
      'API access',
    ],
    mostPopular: true,
  },
  {
    name: 'Business',
    id: 'tier-business',
    href: '/signup?plan=business',
    priceMonthly: '$99',
    priceYearly: '$990',
    description: 'Built for large teams, agencies, and enterprises with advanced needs.',
    features: [
      'Everything in Professional',
      'Custom optimization algorithms',
      'White-label options',
      'Advanced security features',
      'Dedicated account manager',
      'Custom integrations',
      'Unlimited team members',
      'Advanced analytics and reporting',
      'SLA guarantee',
    ],
    mostPopular: false,
  },
]

export function Pricing() {
  return (
    <div id="pricing" className="bg-white py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-4xl text-center">
          <h2 className="text-base font-semibold leading-7 text-primary-600">Pricing</h2>
          <p className="mt-2 text-4xl font-bold tracking-tight text-gray-900 sm:text-5xl">
            Choose the right plan for your needs
          </p>
        </div>
        <p className="mx-auto mt-6 max-w-2xl text-center text-lg leading-8 text-gray-600">
          Start free and scale as you grow. All plans include our core optimization features 
          and are backed by our 6 months of research.
        </p>
        <div className="isolate mx-auto mt-16 grid max-w-md grid-cols-1 gap-y-8 sm:mt-20 lg:mx-0 lg:max-w-none lg:grid-cols-3 lg:gap-x-8">
          {tiers.map((tier, tierIdx) => (
            <div
              key={tier.id}
              className={`
                ${tier.mostPopular ? 'ring-2 ring-primary-600' : 'ring-1 ring-gray-200'}
                ${tierIdx === 0 ? 'rounded-t-3xl sm:rounded-t-none' : ''}
                ${tierIdx === tiers.length - 1 ? 'rounded-b-3xl sm:rounded-b-none' : ''}
                relative rounded-3xl p-8 xl:p-10
              `}
            >
              {tier.mostPopular && (
                <div className="absolute inset-x-0 -top-3 flex justify-center">
                  <div className="rounded-full bg-primary-600 px-4 py-1 text-sm font-medium text-white">
                    Most popular
                  </div>
                </div>
              )}
              <div className="flex items-center justify-between gap-x-4">
                <h3 id={tier.id} className="text-lg font-semibold leading-8 text-gray-900">
                  {tier.name}
                </h3>
              </div>
              <p className="mt-4 text-sm leading-6 text-gray-600">{tier.description}</p>
              <p className="mt-6 flex items-baseline gap-x-1">
                <span className="text-4xl font-bold tracking-tight text-gray-900">
                  {tier.priceMonthly}
                </span>
                <span className="text-sm font-semibold leading-6 text-gray-600">/month</span>
              </p>
              <a
                href={tier.href}
                className={`
                  ${tier.mostPopular
                    ? 'bg-primary-600 text-white shadow-sm hover:bg-primary-500'
                    : 'text-primary-600 ring-1 ring-inset ring-primary-200 hover:ring-primary-300'
                  }
                  mt-6 block rounded-md px-3 py-2 text-center text-sm font-semibold leading-6 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary-600
                `}
              >
                {tier.name === 'Starter' ? 'Get started' : 'Start free trial'}
              </a>
              <ul role="list" className="mt-8 space-y-3 text-sm leading-6 text-gray-600">
                {tier.features.map((feature) => (
                  <li key={feature} className="flex gap-x-3">
                    <CheckIcon className="h-6 w-5 flex-none text-primary-600" aria-hidden="true" />
                    {feature}
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
        <div className="mt-16 text-center">
          <p className="text-sm text-gray-600">
            Need a custom solution?{' '}
            <a href="/contact" className="font-semibold text-primary-600 hover:text-primary-500">
              Contact our sales team
            </a>
          </p>
        </div>
      </div>
    </div>
  )
}