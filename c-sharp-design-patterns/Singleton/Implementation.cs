﻿namespace Singleton
{
    /// <summary>
    /// Singleton
    /// </summary>
    public class Logger
    {
        //private static Logger? _instance;

        // Lazy<T>
        private static readonly Lazy<Logger> _lazyLogger
            = new Lazy<Logger>(()=> new Logger());

        /// <summary>
        /// Instance
        /// </summary>
        public static Logger Instance
        {
            get
            {
                return _lazyLogger.Value;
                //if (_instance == null)
                //{
                //    _instance = new Logger();
                //}
                //return _instance;
            }
        }

        protected Logger()
        {
        }

        /// <summary>
        /// SingletonOperation
        /// </summary>
        public void Log(string message)
        {
            Console.WriteLine($"Message to log: {message}");
        }
    }
}
