import { 
  CpuChipIcon, 
  ChartBarIcon, 
  LightBulbIcon, 
  RocketLaunchIcon,
  ShieldCheckIcon,
  UsersIcon
} from '@heroicons/react/24/outline'

const features = [
  {
    name: 'AI-Powered Optimization',
    description: 'Our advanced algorithms analyze your prompts and apply research-backed techniques to improve performance by up to 25%.',
    icon: CpuChipIcon,
  },
  {
    name: 'Performance Analytics',
    description: 'Track success rates, cost efficiency, and ROI with detailed analytics and benchmarking against industry standards.',
    icon: ChartBarIcon,
  },
  {
    name: 'Proven Techniques',
    description: 'Access 6 months of systematic research including chain-of-thought, role-based prompting, and context optimization.',
    icon: LightBulbIcon,
  },
  {
    name: 'A/B Testing',
    description: 'Compare different prompt variations side-by-side to find the most effective approach for your specific use case.',
    icon: RocketLaunchIcon,
  },
  {
    name: 'Enterprise Security',
    description: 'Bank-grade security with encryption, compliance features, and enterprise-grade infrastructure for peace of mind.',
    icon: ShieldCheckIcon,
  },
  {
    name: 'Team Collaboration',
    description: 'Share prompts, collaborate on optimizations, and maintain version control with your team in dedicated workspaces.',
    icon: UsersIcon,
  },
]

export function Features() {
  return (
    <div id="features" className="py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl lg:text-center">
          <h2 className="text-base font-semibold leading-7 text-primary-600">Research-Backed Platform</h2>
          <p className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            Everything you need to optimize your AI prompts
          </p>
          <p className="mt-6 text-lg leading-8 text-gray-600">
            Built on 6 months of systematic research, our platform combines proven techniques 
            with intelligent automation to help you achieve better AI outcomes.
          </p>
        </div>
        <div className="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
          <dl className="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
            {features.map((feature) => (
              <div key={feature.name} className="flex flex-col">
                <dt className="flex items-center gap-x-3 text-base font-semibold leading-7 text-gray-900">
                  <feature.icon className="h-5 w-5 flex-none text-primary-600" aria-hidden="true" />
                  {feature.name}
                </dt>
                <dd className="mt-4 flex flex-auto flex-col text-base leading-7 text-gray-600">
                  <p className="flex-auto">{feature.description}</p>
                </dd>
              </div>
            ))}
          </dl>
        </div>
      </div>
    </div>
  )
}