import React, { useState } from 'react';
import { Moon, Sun, Send } from 'lucide-react';
import { Switch } from '@/components/ui/switch';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';

const PubAssistant = () => {
  const [darkMode, setDarkMode] = useState(false);
  const [abstract, setAbstract] = useState('');
  const [feedback, setFeedback] = useState('');

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
  };

  const handleSubmit = () => {
    // Here you would typically send the abstract to your backend for processing
    // For this example, we'll just set some dummy feedback
    setFeedback("Your abstract is well-structured. Consider adding more specific details about your methodology.");
  };

  return (
    <div className={`min-h-screen p-8 ${darkMode ? 'bg-gray-900 text-white' : 'bg-gray-100 text-gray-900'}`}>
      <div className="max-w-3xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-3xl font-bold">Pub Assistant</h1>
          <div className="flex items-center space-x-2">
            <Sun className="h-5 w-5" />
            <Switch checked={darkMode} onCheckedChange={toggleDarkMode} />
            <Moon className="h-5 w-5" />
          </div>
        </div>

        <div className="mb-6">
          <h2 className="text-xl font-semibold mb-2">Instructions</h2>
          <p className="text-sm">
            Write or paste your abstract in the text area below. Pub Assistant will analyze your abstract and provide feedback to help you improve it.
          </p>
        </div>

        <Textarea
          placeholder="Enter your abstract here..."
          value={abstract}
          onChange={(e) => setAbstract(e.target.value)}
          className="w-full h-40 mb-4"
        />

        <Button onClick={handleSubmit} className="w-full mb-4">
          <Send className="mr-2 h-4 w-4" /> Get Feedback
        </Button>

        {feedback && (
          <div className={`p-4 rounded-lg ${darkMode ? 'bg-gray-800' : 'bg-white'}`}>
            <h3 className="text-lg font-semibold mb-2">Feedback</h3>
            <p>{feedback}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default PubAssistant;
